import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Course, LabImage, LabLanguage, LanguageInfo, Profile} from '../models/course.model';
import {Observable, of} from 'rxjs';
import {environment} from '../../../environments/environment';
import {delay, map} from 'rxjs/operators';

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

  public setCourseProgress(userId: string, courseId: string, categoryId: string): Observable<any> {
    const payload = {
      userId,
      courseId,
      categoryId
    }
    return this.http.put<any>(environment.API_ENDPOINT + `/api/training/update`, payload, { headers: this.headers })
  }

  public getCourseProgress(userId: string, courseId: string): Observable<string[]> {
    return this.http.get<string[]>(environment.API_ENDPOINT + `/api/training/course/${courseId}/progress/${userId}`, { headers: this.headers })
  }


  public getLanguages(): LanguageInfo[] {
    return [
      {
        code: "python",
        name: "Python"
      },
      {
        code: "java",
        name: "Java"
      },
      {
        code: "js",
        name: "JavaScript"
      },
      {
        code: "net",
        name: "C#"
      },
      {
        code: "ruby",
        name: "Ruby"
      }
    ]
  }

  public getLabImageLanguageCode(labImage: LabImage): LabLanguage {
    if (labImage.net) {
      return "net";
    } else if (labImage.js) {
      return "js"
    } else if (labImage.java) {
      return "java"
    } else if (labImage.python) {
      return "python"
    } else if (labImage.ruby) {
      return "python"
    } else {
      console.error('Unknown language in lab image:', labImage);
      return undefined;
    }
  }
}
