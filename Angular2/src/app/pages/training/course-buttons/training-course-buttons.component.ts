import {Component, OnDestroy, OnInit} from '@angular/core';
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

  constructor(private trainingNavigationService: TrainingNavigationService) { }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.nextButtonText$.subscribe(nextButtonText => {
      this.nextButtonText = nextButtonText;
    }));

    this.subscriptions.push(this.trainingNavigationService.runningLabChanged$.subscribe(lab => {
      this.runningLab = lab;
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
