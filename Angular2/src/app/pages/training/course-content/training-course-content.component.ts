import {Component, Input, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingPersistenceService} from '../../../core/services/training.persistence.service';
import {Course, CourseItem} from '../../../core/models/course.model';

@Component({
  selector: 'app-training-course-content',
  templateUrl: './training-course-content.component.html',
  styleUrls: ['./training-course-content.component.scss']
})
export class TrainingCourseContentComponent implements OnInit {
  @Input() public course: Course;
  private subscriptions: Subscription[] = [];
  public courseItem: CourseItem;
  public markdownPath: string;

  constructor(private trainingPersistenceService: TrainingPersistenceService) { }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingPersistenceService.currentCourseItem$.subscribe(courseItem => {
      this.courseItem = courseItem;
      if (courseItem && courseItem.content && courseItem.content.length > 0) {
        if (courseItem.content[0].slide) {
          this.markdownPath = this.course.assetsPath + courseItem.content[0].slide;
        } else if (courseItem.content[0].questionnaire) {
          this.markdownPath = this.course.assetsPath + courseItem.content[0].questionnaire;
        }
      }
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
