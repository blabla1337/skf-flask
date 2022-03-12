import {Component, Input, OnInit} from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-training-content-video',
  templateUrl: './training-content-video.component.html',
  styleUrls: ['./training-content-video.component.scss']
})
export class TrainingContentVideoComponent implements OnInit {
  private _videoPath: string;
  get videoPath(): string {
    return this._videoPath;
  }
  @Input() set videoPath(value: string) {
    this._videoPath = value;
    this.updateVideo();
  }
  constructor(public domSanitizer: DomSanitizer) { }

  ngOnInit(): void {
  }

  private updateVideo() {

  }
}
