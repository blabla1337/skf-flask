import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Knowledgebase } from '../models/knowledgebase';
import { Observable } from 'rxjs/Rx';
import { Question_sprint } from '../models/question_sprint'
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class QuestionsSprintService {

  constructor(private http: Http) { }

  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN});

  getSprintQuestions(checklistType:number) {
    return this.http.get(environment.API_ENDPOINT + `/questions_sprint/items/${checklistType}`, { headers: this.postHeaders })
      .map(response => response.json().items)
  }

  newSprint(questions: Question_sprint[]): Observable<Question_sprint[]> {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_sprint/store', JSON.stringify({ questions }),
      { headers: this.postHeaders })
      .map(response => {
        return response.json()
      });
  }
}