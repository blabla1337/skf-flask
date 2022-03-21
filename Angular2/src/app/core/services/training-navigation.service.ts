import {Injectable} from '@angular/core';
import {CourseItem} from '../models/course.model';
import {BehaviorSubject, Subject} from 'rxjs';


@Injectable({providedIn: 'root'})
export class TrainingNavigationService {
  private nextClickedSubject: Subject<void> = new Subject<void>();
  public nextClicked$ = this.nextClickedSubject.asObservable();

  public onNextClicked() {
    this.nextClickedSubject.next();
  }



  // TODO IB !!!! rename
  private currentCourseItemSubject: BehaviorSubject<CourseItem> = new BehaviorSubject<CourseItem>(undefined);
  public currentCourseItem$ = this.currentCourseItemSubject.asObservable();

  public setSelectedCourseItem(courseItem: CourseItem) {
    this.currentCourseItemSubject.next(courseItem);
  }

  // private currentProfileSubject: BehaviorSubject<Profile> = new BehaviorSubject<Profile>(undefined);
  // public currentProfile$ = this.currentProfileSubject.asObservable();
  //
  // public setSelectedProfile(profile: Profile) {
  //   this.currentProfileSubject.next(profile);
  // }

}
