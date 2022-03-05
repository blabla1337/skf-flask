import { Component, OnInit } from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingPersistenceService} from '../../../core/services/training.persistence.service';
import {CourseItem} from '../../../core/models/course.model';

@Component({
  selector: 'app-training-course-content',
  templateUrl: './training-course-content.component.html',
  styleUrls: ['./training-course-content.component.scss']
})
export class TrainingCourseContentComponent implements OnInit {
  private subscriptions: Subscription[] = [];
  public courseItem: CourseItem;

  constructor(private trainingPersistenceService: TrainingPersistenceService) { }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingPersistenceService.currentCourseItem$.subscribe(courseItem => {
      this.courseItem = courseItem;
    }));
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if(sub) {
        sub.unsubscribe();
      }
    });
  }
}
