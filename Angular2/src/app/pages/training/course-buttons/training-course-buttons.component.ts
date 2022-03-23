import {Component, OnDestroy, OnInit} from '@angular/core';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {Subscription} from 'rxjs';

@Component({
  selector: 'app-training-course-buttons',
  templateUrl: './training-course-buttons.component.html',
  styleUrls: ['./training-course-buttons.component.scss']
})
export class TrainingCourseButtonsComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];
  public nextButtonText: string = "Next";
  public contentIsLab: boolean;
  public labHint: string;
  public labWriteup: string;

  constructor(private trainingNavigationService: TrainingNavigationService) { }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.nextButtonText$.subscribe(nextButtonText => {
      this.nextButtonText = nextButtonText;
    }));

    this.subscriptions.push(this.trainingNavigationService.currentContentItemChanged$.subscribe(contentItem => {
      if (contentItem && contentItem.lab) {
        this.contentIsLab = true;
        this.labHint = contentItem.lab.hint;
        this.labWriteup = contentItem.lab.writeup;
      } else {
        this.contentIsLab = false;
        this.labHint = undefined;
        this.labWriteup = undefined;
      }
    }))
  }

  onNext() {
    this.trainingNavigationService.raiseNextClicked();
  }

  onRestartLab() {
    console.log('TODO IB !!!! onRestartLab');
  }

  onShowHint() {
    console.log('TODO IB !!!! onShowHint');
  }

  onShowWriteUp() {
    console.log('TODO IB !!!! onShowWriteUp');
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }

}
