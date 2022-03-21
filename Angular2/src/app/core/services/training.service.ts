import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Course, Profile} from '../models/course.model';
import {Observable, of} from 'rxjs';
import {environment} from '../../../environments/environment';
import {map} from 'rxjs/operators';

@Injectable({providedIn: 'root'})
export class TrainingService {
  constructor(private http: HttpClient) { }
  public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

  public getProfiles(): Observable<Profile[]> {
    return this.http
      .get<any>(environment.API_ENDPOINT + `/api/training/profiles`, { headers: this.headers })
      .pipe(map(x => x.profiles as Profile[]))
  }

  public getProfileInfo(profileId: string): Observable<Profile> {
    return this.http.get<Profile>(environment.API_ENDPOINT + `/api/training/profile/${profileId}`, { headers: this.headers })
  }

  public getCourse(courseId: string): Observable<Course> {
    return this.http.get<Course>(environment.API_ENDPOINT + `/api/training/course/${courseId}`, { headers: this.headers })
  }

  // TODO IB !!!! implement and test this
  public setCourseProgress(userId: string, courseId: string, categoryId: string): Observable<boolean> {
    return of(true)
  }

  // TODO IB !!!! implement and test this
  public getCourseProgress(userId: string, courseId: string): Observable<string[]> {
    return of([])
  }
}
