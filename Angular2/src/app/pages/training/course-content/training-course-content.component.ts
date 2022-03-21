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
  public showLab: boolean;

  constructor(private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.currentCourseItemChanged$.subscribe(courseItem => {
      this.courseItem = courseItem;
      this.markdownPath = undefined;
      this.videoPath = undefined;
      this.showLab = false;
      if (courseItem && courseItem.content && courseItem.content.length > 0) {
        if (courseItem.content[0].slide) {
          this.markdownPath = this.course.assetsPath + courseItem.content[0].slide;
        } else if (courseItem.content[0].questionnaire) {
          this.markdownPath = this.course.assetsPath + courseItem.content[0].questionnaire;
        } else if (courseItem.content[0].video) {
          this.videoPath = courseItem.content[0].video;
        } else if (courseItem.content[0].lab) {
          this.showLab = true;
        }
      }
    }));

    this.subscriptions.push(this.trainingNavigationService.nextContentItem$.subscribe(() => {
      console.log("TODO IB !!!! nextContentItem$ in course content");
      // TODO IB !!!! 1 we should display first all content
      this.trainingNavigationService.raiseNextCourseItem();
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
