import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Knowledgebase } from '../models/knowledgebase';
import { Observable } from 'rxjs/Rx';
import { Question_sprint } from '../models/question_sprint'
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';

@Injectable()
export class QuestionsSprintService { 

  constructor(private http: Http) { }
  public putHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN});

  getSprintQuestions() {
    return this.http.get(environment.API_ENDPOINT + '/questions_sprint/items')
      .map(response => response.json().items)
  }

  newSprintQuestion(projectID: number, question_sprint_ID: number,  result: string, sprintID: string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_sprint/store', JSON.stringify({
        projectID: projectID,
        question_sprint_ID: question_sprint_ID,
        sprintID: sprintID,
        result: result
      }),
      { headers: this.putHeaders })
      .map(a => { return a.json() });
  }  

}