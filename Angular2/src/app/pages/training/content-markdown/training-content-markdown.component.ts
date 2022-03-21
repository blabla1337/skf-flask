import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {NgxSpinnerService} from 'ngx-spinner';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';

@Component({
  selector: 'app-training-content-markdown',
  templateUrl: './training-content-markdown.component.html',
  styleUrls: ['./training-content-markdown.component.scss']
})
export class TrainingContentMarkdownComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];
  private _markdownPath: string;
  get markdownPath(): string {
    return this._markdownPath;
  }

  @Input() set markdownPath(value: string) {
    this._markdownPath = value;
    this.updateMarkdown();
  }

  public data: string;

  constructor(private httpClient: HttpClient,
              private spinner: NgxSpinnerService,
              private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      console.log('TODO IB !!!! nextClicked$ in markdown');
      // TODO IB !!!! raise only after all slides are displayed
      this.trainingNavigationService.raiseNextContentItem();
    }));
  }

  onReady() {
  }

  private updateMarkdown() {
    const headers = new HttpHeaders({'Content-Type': 'text/plain; charset=utf-8'});
    this.data = undefined;
    this.spinner.show();

    this.httpClient.get(this._markdownPath, {headers, responseType: 'text'})
      .subscribe(data => {
        this.spinner.hide();
        this.data = data;
      }, (error) => {
        this.spinner.hide();
        console.error(`Could not load markdown data at path ${this._markdownPath}. Error: `, error);
      });
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
