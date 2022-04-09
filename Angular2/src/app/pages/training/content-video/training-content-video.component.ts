import {Component, Input, OnDestroy, OnInit} from '@angular/core';
import {DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';

@Component({
  selector: 'app-training-content-video',
  templateUrl: './training-content-video.component.html',
  styleUrls: ['./training-content-video.component.scss']
})
export class TrainingContentVideoComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];
  public safeVideoPath: SafeResourceUrl;
  private _videoPath: string;
  get videoPath(): string {
    return this._videoPath;
  }

  @Input() set videoPath(value: string) {
    this._videoPath = this.addAutoplayIfMissing(value);
    this.safeVideoPath = this.domSanitizer.bypassSecurityTrustResourceUrl(this._videoPath);
  }

  constructor(private domSanitizer: DomSanitizer,
              private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    this.trainingNavigationService.setNextSlideType("None");

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      this.trainingNavigationService.raiseNextContentItem();
    }));
  }

  addAutoplayIfMissing(inputUrl: string): string {
    const url: URL = new URL(inputUrl);
    url.searchParams.set('autoplay', '1');
    return url.toString();
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
