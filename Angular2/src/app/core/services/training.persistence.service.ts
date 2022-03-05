import {Injectable} from '@angular/core';
import {CourseItem} from '../models/course.model';
import {BehaviorSubject} from 'rxjs';


@Injectable({providedIn: 'root'})
export class TrainingPersistenceService {

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
