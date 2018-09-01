import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Checklist } from '../models/checklist';
import { Observable } from 'rxjs/Rx';
import { Question_post } from '../models/question_post'
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';


@Injectable()
export class ChecklistService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getChecklist(id: number): Observable<Checklist[]> {
    return this.http.get(environment.API_ENDPOINT + `/checklist/level/${id}`, { headers: this.headers })
      .map(response => response.json().items)
  }

/*
for next release!
 newChecklist(questions: Question_post[]): Observable<Question_post[]> {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_post/store', JSON.stringify({ questions }),
      { headers: this.postHeaders })
      .map(a => {
        return a.json()
      });
  }
*/

}