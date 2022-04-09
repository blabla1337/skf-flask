import {Injectable} from '@angular/core';
import {CourseItem, ContentItemType, SlideType, ContentItem, Lab} from '../models/course.model';
import {BehaviorSubject, Subject} from 'rxjs';

@Injectable({providedIn: 'root'})
export class TrainingNavigationService {
  // Event raised when the next button is clicked.
  // Try to go to next slide, if none, go to next content item
  private nextClickedSubject: Subject<void> = new Subject<void>();
  public nextClicked$ = this.nextClickedSubject.asObservable();
  public raiseNextClicked() {
    this.nextClickedSubject.next();
  }

  // Event raised when we should display the next content for a Topic/Category
  // Try to go to next content item, if none, go to next Topic/Category
  private nextContentItemSubject: Subject<void> = new Subject<void>();
  public nextContentItem$ = this.nextContentItemSubject.asObservable();
  public raiseNextContentItem() {
    this.nextContentItemSubject.next();
  }

  // Event raised when we should go to next Topic/Category
  // Try to go to next course item, if any
  private nextCourseItemSubject: Subject<void> = new Subject<void>();
  public nextCourseItem$ = this.nextCourseItemSubject.asObservable();
  public raiseNextCourseItem() {
    this.nextCourseItemSubject.next();
  }

  // event raised when a new Topic/Category is selected
  private currentCourseItemChangedSubject: Subject<CourseItem> = new Subject<CourseItem>();
  public currentCourseItemChanged$ = this.currentCourseItemChangedSubject.asObservable();
  public raiseCurrentCourseItemChanged(courseItem: CourseItem) {
    this.currentCourseItemChangedSubject.next(courseItem);
  }

  private nextSlideTypeSubject: BehaviorSubject<SlideType> = new BehaviorSubject<SlideType>("Unknown");
  public nextSlideType$ = this.nextSlideTypeSubject.asObservable();
  public setNextSlideType(nextSlideType: SlideType) {
    this.nextSlideTypeSubject.next(nextSlideType);
    this.computeNextButtonText();
  }

  private nextContentItemTypeSubject: BehaviorSubject<ContentItemType> = new BehaviorSubject<ContentItemType>("None");
  public nextContentItemType$ = this.nextContentItemTypeSubject.asObservable();
  public setNextContentItemType(nextContentItemType: ContentItemType) {
    this.nextContentItemTypeSubject.next(nextContentItemType);
    this.computeNextButtonText();
  }

  private nextButtonTextSubject: BehaviorSubject<string> = new BehaviorSubject<string>("Next");
  public nextButtonText$ = this.nextButtonTextSubject.asObservable();
  private computeNextButtonText() {
    const nextSlideType = this.nextSlideTypeSubject.getValue();
    const nextContentItemType = this.nextContentItemTypeSubject.getValue();
    if (nextSlideType === "Question") {
      this.nextButtonTextSubject.next("Next Question");
    } else if (nextSlideType === "Answer") {
      this.nextButtonTextSubject.next("Show Answer");
    } else if (nextSlideType === "Slide") {
      this.nextButtonTextSubject.next("Next Slide");
    } else if (nextSlideType === "Unknown") {
      this.nextButtonTextSubject.next("Next");
    } else if (nextContentItemType === "Slides") {
      this.nextButtonTextSubject.next("Next Slide");
    } else if (nextContentItemType === "Questionnaire") {
      this.nextButtonTextSubject.next("Start Questionaire");
    } else if (nextContentItemType === "Lab") {
      this.nextButtonTextSubject.next("Start Lab");
    } else {
      this.nextButtonTextSubject.next("Next");
    }
  }

  private markCategoryAsSeenSubject: Subject<string> = new Subject<string>();
  public markCategoryAsSeen$ = this.markCategoryAsSeenSubject.asObservable();
  public raiseMarkCategoryAsSeen(categoryId: string) {
    this.markCategoryAsSeenSubject.next(categoryId);
  }

  private runningLabChangedSubject: BehaviorSubject<Lab> = new BehaviorSubject<Lab>(undefined);
  public runningLabChanged$ = this.runningLabChangedSubject.asObservable();
  public raiseRunningLabChanged(lab: Lab) {
    this.runningLabChangedSubject.next(lab);
  }

  private restartLabSubject: Subject<void> = new Subject<void>();
  public restartLab$ = this.restartLabSubject.asObservable();
  public raiseRestartLab() {
    this.restartLabSubject.next();
  }

  private openWriteUpSubject: Subject<void> = new Subject<void>();
  public openWriteUp$ = this.openWriteUpSubject.asObservable();
  public raiseOpenWriteUp() {
    this.openWriteUpSubject.next();
  }

  private labHintClickedSubject: Subject<void> = new Subject<void>();
  public labHintClicked$ = this.labHintClickedSubject.asObservable();
  public raiseLabHintClicked() {
    this.labHintClickedSubject.next();
  }

  private fullScreenChangedSubject: BehaviorSubject<boolean> = new BehaviorSubject<boolean>(undefined);
  public fullScreenChanged$ = this.fullScreenChangedSubject.asObservable();
  public raiseFullScreenChanged(isFullScreen: boolean) {
    const currentValue = this.fullScreenChangedSubject.getValue();
    if (isFullScreen !== currentValue) {
      this.fullScreenChangedSubject.next(isFullScreen);
    }
  }
}
