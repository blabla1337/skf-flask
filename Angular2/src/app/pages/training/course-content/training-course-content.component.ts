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
  private currentContentItem: number;

  constructor(private trainingNavigationService: TrainingNavigationService) {
  }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.currentCourseItemChanged$.subscribe(courseItem => {
      this.courseItem = courseItem;
      this.currentContentItem = 0;
      this.prepareContentDisplay();
    }));

    this.subscriptions.push(this.trainingNavigationService.nextContentItem$.subscribe(() => {
      console.log("TODO IB !!!! nextContentItem$ in course content");
      if (this.currentContentItem < this.courseItem.content.length - 1) {
        this.currentContentItem++;
        this.prepareContentDisplay();
      } else {
        this.trainingNavigationService.raiseNextCourseItem();
      }
    }));
  }

  private prepareContentDisplay() {
    this.markdownPath = undefined;
    this.videoPath = undefined;
    this.showLab = false;

    if (this.courseItem && this.courseItem.content && this.currentContentItem < this.courseItem.content.length) {
      if (this.courseItem.content[this.currentContentItem].slide) {
        this.markdownPath = this.course.assetsPath + this.courseItem.content[this.currentContentItem].slide;
      } else if (this.courseItem.content[this.currentContentItem].questionnaire) {
        this.markdownPath = this.course.assetsPath + this.courseItem.content[this.currentContentItem].questionnaire;
      } else if (this.courseItem.content[this.currentContentItem].video) {
        this.videoPath = this.courseItem.content[this.currentContentItem].video;
      } else if (this.courseItem.content[this.currentContentItem].lab) {
        this.showLab = true;
      }
    }
  }

  ngOnDestroy(): void {
    this.subscriptions.forEach(sub => {
      if (sub) {
        sub.unsubscribe();
      }
    });
  }
}
