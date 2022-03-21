import {Component, Input, OnInit} from '@angular/core';
import {DomSanitizer, SafeResourceUrl} from '@angular/platform-browser';

@Component({
  selector: 'app-training-content-video',
  templateUrl: './training-content-video.component.html',
  styleUrls: ['./training-content-video.component.scss']
})
export class TrainingContentVideoComponent implements OnInit {
  public safeVideoPath: SafeResourceUrl;
  private _videoPath: string;
  get videoPath(): string {
    return this._videoPath;
  }

  @Input() set videoPath(value: string) {
    this._videoPath = value;
    // TODO IB !!!! autoplay? this._videoPath = this.addAutoplayIfMissing(value);
    this.safeVideoPath = this.domSanitizer.bypassSecurityTrustResourceUrl(this._videoPath);
  }

  constructor(private domSanitizer: DomSanitizer) {
  }

  ngOnInit(): void {
  }

  addAutoplayIfMissing(inputUrl: string): string {
    const url: URL = new URL(inputUrl);
    url.searchParams.set('autoplay', '1');
    return url.toString();
  }
}
