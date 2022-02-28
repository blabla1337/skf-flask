import {Profile} from '../models/course.model';
import {Injectable} from '@angular/core';
import {BehaviorSubject} from 'rxjs';

@Injectable({providedIn: 'root'})
export class TrainingPersistenceService {

  private currentProfileSubject: BehaviorSubject<Profile> = new BehaviorSubject<Profile>(undefined);
  public currentProfile$ = this.currentProfileSubject.asObservable();

  public setSelectedProfile(profile: Profile) {
    this.currentProfileSubject.next(profile);
  }
}
