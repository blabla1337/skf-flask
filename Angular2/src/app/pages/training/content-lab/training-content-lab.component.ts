import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';

@Component({
  selector: 'app-training-content-lab',
  templateUrl: './training-content-lab.component.html',
  styleUrls: ['./training-content-lab.component.scss']
})
export class TrainingContentLabComponent implements OnInit, OnDestroy {
  private subscriptions: Subscription[] = [];

  constructor(private trainingNavigationService: TrainingNavigationService) { }

  ngOnInit(): void {
    this.trainingNavigationService.setNextSlideType("None");

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      console.log('TODO IB !!!! nextClicked$ in lab');
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
