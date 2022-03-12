import {Component, Input, OnInit} from '@angular/core';
import {DomSanitizer} from '@angular/platform-browser';

@Component({
  selector: 'app-training-content-video',
  templateUrl: './training-content-video.component.html',
  styleUrls: ['./training-content-video.component.scss']
})
export class TrainingContentVideoComponent implements OnInit {
  @Input() videoPath;
  constructor(public domSanitizer: DomSanitizer) { }

  ngOnInit(): void {
  }
}
