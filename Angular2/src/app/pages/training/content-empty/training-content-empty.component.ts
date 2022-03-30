import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';

@Component({
  selector: 'app-training-content-empty',
  templateUrl: './training-content-empty.component.html',
  styleUrls: ['./training-content-empty.component.scss']
})
export class TrainingContentEmptyComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];

  constructor(private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    this.trainingNavigationService.setNextSlideType("None");

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      this.trainingNavigationService.raiseNextContentItem();
    }));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
