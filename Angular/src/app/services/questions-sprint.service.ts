
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Knowledgebase } from '../models/knowledgebase';
import { Observable } from 'rxjs';
import { Question_sprint } from '../models/question_sprint'
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class QuestionsSprintService {

  constructor(private http: Http) { }

  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN});

  getSprintQuestions(checklistType:number) {
    return this.http.get(environment.API_ENDPOINT + `/questions_sprint/items/${checklistType}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  newSprint(questions: Question_sprint[]): Observable<Question_sprint[]> {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_sprint/store', JSON.stringify({ questions }),
      { headers: this.postHeaders }).pipe(
      map(response => {
        return response.json()
      }));
  }

  updatePre(id: number, questions: Question_sprint[]) {
    return this.http.put(environment.API_ENDPOINT + `/questions_sprint/update/${id}`, JSON.stringify({ questions }),
      { headers: this.postHeaders }).pipe(
      map(response => response.json()))
  }

  newQuestion(checklist_type:number, questionName:string, ) {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_sprint/item/new', JSON.stringify({ question:questionName, checklist_type:checklist_type }),
      { headers: this.postHeaders }).pipe(
      map(response => { return response.json() }));
  }

  updateQuestion(checklist_type:number, questionName:string, questionID:number) {
    return this.http
      .put(environment.API_ENDPOINT + `/questions_sprint/item/update/${questionID}`, JSON.stringify({ question:questionName, checklist_type:checklist_type}),
      { headers: this.postHeaders }).pipe(
      map(response => { return response.json() }));
  }

  deleteQuestion(id: number) {
    const url = environment.API_ENDPOINT + `/questions_sprint/item/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
        data => data,
        error => console.log("failed to delete checklist item")))
  }

  getChecklistItemsOnPreQuestionID(preQuestionID:number) {
    return this.http.get(environment.API_ENDPOINT + `/checklist/item/question_sprint/${preQuestionID}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

}