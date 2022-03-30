import {Component, HostListener, OnDestroy, OnInit} from '@angular/core';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {Subscription} from 'rxjs';
import {Lab} from '../../../core/models/course.model';

@Component({
  selector: 'app-training-course-buttons',
  templateUrl: './training-course-buttons.component.html',
  styleUrls: ['./training-course-buttons.component.scss']
})
export class TrainingCourseButtonsComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];
  public nextButtonText: string = "Next";
  public runningLab: Lab;
  public isFullScreen: boolean;

  constructor(private trainingNavigationService: TrainingNavigationService) { }

  ngOnInit(): void {
    this.checkFullScreen();

    this.subscriptions.push(this.trainingNavigationService.nextButtonText$.subscribe(nextButtonText => {
      this.nextButtonText = nextButtonText;
    }));

    this.subscriptions.push(this.trainingNavigationService.runningLabChanged$.subscribe(lab => {
      this.runningLab = lab;
    }));
  }

  onNext() {
    this.trainingNavigationService.raiseNextClicked();
  }

  onRestartLab() {
    this.trainingNavigationService.raiseRestartLab();
  }

  onShowWriteUp() {
    if (this.runningLab) {
      window.open(this.runningLab.writeup, "_blank");
    }
  }

  @HostListener('document:fullscreenchange', ['$event'])
  @HostListener('document:mozfullscreenchange', ['$event'])
  @HostListener('document:webkitfullscreenchange', ['$event'])
  @HostListener('document:msfullscreenchange', ['$event'])
  private fullscreenchange(e: any) {
    this.checkFullScreen();
  }

  private checkFullScreen() {
    const doc = document as any;
    this.isFullScreen = doc.fullscreenElement
      || doc.webkitFullscreenElement
      || doc.mozFullScreenElement;
  }

  onOpenFullScreen() {
    this.trainingNavigationService.raiseOpenFullScreen();
  }

  onCloseFullScreen() {
    this.trainingNavigationService.raiseCloseFullScreen();
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
