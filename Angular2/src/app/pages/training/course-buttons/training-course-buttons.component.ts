import { Component, OnInit } from '@angular/core';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';

@Component({
  selector: 'app-training-course-buttons',
  templateUrl: './training-course-buttons.component.html',
  styleUrls: ['./training-course-buttons.component.scss']
})
export class TrainingCourseButtonsComponent implements OnInit {

  constructor(private trainingNavigationService: TrainingNavigationService) { }

  ngOnInit(): void {
  }

  onNext() {
    this.trainingNavigationService.onNextClicked();
  }
}
