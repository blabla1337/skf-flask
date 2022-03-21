import {Injectable} from '@angular/core';
import {CourseItem} from '../models/course.model';
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
}
