import {Component, Input, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {TrainingNavigationService} from '../../../core/services/training-navigation.service';
import {ContentItemType, Course, CourseItem} from '../../../core/models/course.model';
import {TrainingService} from '../../../core/services/training.service';

@Component({
  selector: 'app-training-course-content',
  templateUrl: './training-course-content.component.html',
  styleUrls: ['./training-course-content.component.scss']
})
export class TrainingCourseContentComponent implements OnInit {
  @Input() public course: Course;
  @Input() public userId: string;
  private subscriptions: Subscription[] = [];
  public courseItem: CourseItem;
  public markdownPath: string;
  public videoPath: string;
  private currentContentItemIndex: number;
  public contentItemType: ContentItemType;

  constructor(private trainingNavigationService: TrainingNavigationService,
              private trainingService: TrainingService) {
  }

  ngOnInit(): void {
    this.subscriptions.push(this.trainingNavigationService.currentCourseItemChanged$.subscribe(courseItem => {
      this.courseItem = courseItem;
      this.currentContentItemIndex = 0;
      this.prepareContentDisplay();
    }));

    this.subscriptions.push(this.trainingNavigationService.nextContentItem$.subscribe(() => {
      console.log("TODO IB !!!! nextContentItem$ in course content");
      if (this.currentContentItemIndex < this.courseItem.content.length - 1) {
        this.currentContentItemIndex++;
        this.prepareContentDisplay();
      } else {
        this.trainingNavigationService.raiseNextCourseItem();
      }
    }));
  }

  private prepareContentDisplay() {
    this.markdownPath = undefined;
    this.videoPath = undefined;
    this.contentItemType = "None";

    if (this.courseItem && this.courseItem.content) {
      if (this.currentContentItemIndex < this.courseItem.content.length) {
        const currentContentItem = this.courseItem.content[this.currentContentItemIndex];
        if (currentContentItem.slide) {
          this.markdownPath = this.course.assetsPath + currentContentItem.slide;
          this.contentItemType = "Slides";
        } else if (currentContentItem.questionnaire) {
          this.markdownPath = this.course.assetsPath + currentContentItem.questionnaire;
          this.contentItemType = "Questionnaire";
        } else if (currentContentItem.video) {
          this.videoPath = currentContentItem.video;
          this.contentItemType = "Video";
        } else if (currentContentItem.lab) {
          this.contentItemType = "Lab";
        }
      }

      if (this.currentContentItemIndex < this.courseItem.content.length - 1) {
        const nextContentItem = this.courseItem.content[this.currentContentItemIndex + 1];
        if (nextContentItem.slide) {
          this.trainingNavigationService.setNextContentItemType("Slides");
        } else if (nextContentItem.questionnaire) {
          this.trainingNavigationService.setNextContentItemType("Questionnaire");
        } else if (nextContentItem.video) {
          this.trainingNavigationService.setNextContentItemType("Video");
        } else if (nextContentItem.lab) {
          this.trainingNavigationService.setNextContentItemType("Lab");
        } else {
          this.trainingNavigationService.setNextContentItemType("None");
        }
      } else {
        this.trainingNavigationService.setNextContentItemType("None");
        console.log('TODO IB !!!! last course content. call setCourseProgress');
        console.log('TODO IB !!!! this.courseItem.courseItemType', this.courseItem.courseItemType);
        if (this.userId !== undefined && this.userId !== "" && this.courseItem.courseItemType === "Category") {
          this.subscriptions.push(this.trainingService.setCourseProgress(this.userId, this.course.id, this.courseItem.id)
            .subscribe(() => {})
          );
        }
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
