import {Component, Input, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
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
  public videoPath: string;

  constructor(private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.currentCourseItem$.subscribe(courseItem => {
      this.courseItem = courseItem;
      this.markdownPath = undefined;
      this.videoPath = undefined;
      if (courseItem && courseItem.content && courseItem.content.length > 0) {
        if (courseItem.content[0].slide) {
          this.markdownPath = this.course.assetsPath + courseItem.content[0].slide;
        } else if (courseItem.content[0].questionnaire) {
          this.markdownPath = this.course.assetsPath + courseItem.content[0].questionnaire;
        } else if (courseItem.content[0].video) {
          this.videoPath = courseItem.content[0].video;
        }
      }
    }));

    this.subscriptions.push(this.trainingNavigationService.nextClicked$.subscribe(() => {
      console.log('TODO IB !!!! nextClicked$');
    }))
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
