import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Knowledgebase } from '../models/knowledgebase';
import { Observable } from 'rxjs/Rx';
import { Question_sprint } from '../models/question_sprint'
import 'rxjs/add/operator/toPromise';

@Injectable()
export class QuestionsSprintService {

  constructor(private http: Http) { }

  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });

  getSprintQuestions() {
    return this.http.get("http://127.0.0.1:8888/api/questions_sprint/items")
      .map(response => response.json().items)
  }

  newSprint(questions:Question_sprint[]): Observable<Question_sprint[]> {  
    return this.http
      .put('http://127.0.0.1:8888/api/questions_sprint/store', JSON.stringify({questions}),
      { headers: this.postHeaders })
      .map(response => { 
        return response.json()});
  }
}