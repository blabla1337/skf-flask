import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Question_pre } from '../models/question_pre';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';

@Injectable()
export class QuestionPreService {

  constructor(private http: Http) { }
  public putHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getPreQuestions() {
    return this.http.get(environment.API_ENDPOINT + '/questions_pre/items')
      .map(response => response.json().items)
  }

  newProject(projectID: number, question_pre_ID: number,  result: string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_pre/store', JSON.stringify({
        projectID: projectID,
        question_pre_ID: question_pre_ID,
        result: result
      }),
      { headers: this.putHeaders })
      .map(a => { return a.json() });
  } 
  
  updatePre(id: number, questions: Question_pre[]) {
    return this.http.put(environment.API_ENDPOINT + `/questions_pre/update/${id}`, JSON.stringify({ questions }),
      { headers: this.putHeaders })
      .map(response => response.json())
  }

}