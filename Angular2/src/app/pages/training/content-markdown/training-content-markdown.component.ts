import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NgxSpinnerService} from 'ngx-spinner';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {ContentItemType} from '../../../core/models/course.model';
import {MarkdownService} from 'ngx-markdown';
import {Renderer} from 'marked';

const MARKDOWN_SPLIT_MARKER = "-----SPLIT-----";

@Component({
  selector: 'app-training-content-markdown',
  templateUrl: './training-content-markdown.component.html',
  styleUrls: ['./training-content-markdown.component.scss']
})
export class TrainingContentMarkdownComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];
  private _markdownPath: string;
  @Input() contentItemType: ContentItemType;
  get markdownPath(): string {
    return this._markdownPath;
  }

  @Input() set markdownPath(value: string) {
    this._markdownPath = value;
    this.setMarkdownBaseUrl();
    this.updateMarkdown();
  }

  public currentDataSlideIndex: number;
  public dataSlides: string[] = [];
  public currentDataSlide: string;
  private markdownOriginalRenderer: Renderer;

  constructor(private httpClient: HttpClient,
              private spinner: NgxSpinnerService,
              private markdownService: MarkdownService,
              private trainingNavigationService: TrainingNavigationService) {
    this.initMarkdownRenderer();
  }

  ngOnInit(): void {
    this.trainingNavigationService.setNextSlideType("Unknown");

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      if (this.dataSlides && this.currentDataSlideIndex < this.dataSlides.length - 1) {
        this.currentDataSlideIndex++;
        this.prepareDataSlide();
      } else {
        this.trainingNavigationService.raiseNextContentItem();
      }
    }));
  }


  private initMarkdownRenderer() {
    this.markdownOriginalRenderer = new Renderer();
    this.markdownService.renderer.link = (href: string | null, title: string | null, text: string) => {
      if (href.startsWith("#")) {
        return this.markdownOriginalRenderer.text(text??"");
      } else {
        const renderedLink = this.markdownOriginalRenderer.link(href, title, text);
        return renderedLink.replace(/^(<a)/, "<a target='_blank'");
      }
    }
    this.markdownService.renderer.image = (href: string | null, title: string | null, text: string) => {
      const renderedImage = this.markdownOriginalRenderer.image(href, title, text);
      return renderedImage.replace(/^(<img)/, "<img class='max-width-100p'")
    }
  }

  private setMarkdownBaseUrl() {
    const lastSlashIndex = this._markdownPath.lastIndexOf('/');
    if (lastSlashIndex !== -1) {
      const baseUrl = this._markdownPath.substr(0, lastSlashIndex + 1);
      this.markdownService.options = {
        baseUrl
      };
      this.markdownOriginalRenderer.options = {
        baseUrl
      }
    }
  }

  onReady() {
  }

  private updateMarkdown() {
    const headers = new HttpHeaders({'Content-Type': 'text/plain; charset=utf-8'});
    this.dataSlides = [];
    this.currentDataSlideIndex = 0;
    this.currentDataSlide = undefined;
    this.spinner.show();

    this.httpClient.get(this._markdownPath, {headers, responseType: 'text'})
      .subscribe(data => {
        this.spinner.hide();
        this.dataSlides = data.split(MARKDOWN_SPLIT_MARKER);
        this.prepareDataSlide();
      }, (error) => {
        this.spinner.hide();
        console.error(`Could not load markdown data at path ${this._markdownPath}. Error: `, error);
      });
  }

  private prepareDataSlide() {
    if (this.dataSlides) {

      if (this.currentDataSlideIndex < this.dataSlides.length) {
        this.currentDataSlide = this.dataSlides[this.currentDataSlideIndex];
      }

      if (this.currentDataSlideIndex < this.dataSlides.length - 1) {
        if (this.contentItemType === "Slides") {
          this.trainingNavigationService.setNextSlideType("Slide");
        } else if (this.contentItemType === "Questionnaire") {
          if (this.currentDataSlideIndex % 2 === 0) {
            this.trainingNavigationService.setNextSlideType("Answer");
          } else {
            this.trainingNavigationService.setNextSlideType("Question");
          }
        } else {
          this.trainingNavigationService.setNextSlideType("None");
        }
      } else {
        this.trainingNavigationService.setNextSlideType("None");
      }
    }
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
