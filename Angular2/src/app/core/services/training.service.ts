import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Course, CourseInfo, Profile} from '../models/course.model';
import {Observable, of} from 'rxjs';
import _ from "lodash";
import {environment} from '../../../environments/environment';
import {map} from 'rxjs/operators';

@Injectable({providedIn: 'root'})
export class TrainingService {
  constructor(private http: HttpClient) { }
  public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

  // TODO IB !!!! move to persistence
  private seenItems: string[] = [];

  public getProfiles(): Observable<Profile[]> {
    return this.http
      .get<any>(environment.API_ENDPOINT + `/api/training/profiles`, { headers: this.headers })
      .pipe(map(x => x.profiles as Profile[]))
  }

  public getProfileInfo(profileId: string): Observable<Profile> {
    return this.http.get<Profile>(environment.API_ENDPOINT + `/api/training/profile/${profileId}`, { headers: this.headers })
  }

  // TODO IB !!!! This might not be needed
  public getCourseInfo(courseId: string): Observable<CourseInfo> {
    return this.http.get<CourseInfo>(environment.API_ENDPOINT + `/api/training/courseinfo/${courseId}`, { headers: this.headers })
  }

  public getCourse(courseId: string): Observable<Course> {
    return this.http.get<Course>(environment.API_ENDPOINT + `/api/training/course/${courseId}`, { headers: this.headers })
  }

  // TODO IB !!!! test this
  public setCourseSeenItems(courseId: string, itemIds: string[]): Observable<boolean> {
    this.seenItems.push(...itemIds)
    this.seenItems = _.uniq(this.seenItems)
    return of(true)
  }

  // TODO IB !!!! test this
  public getCourseSeenItems(courseId: string): Observable<string[]> {
    return of(this.seenItems)
  }
}
