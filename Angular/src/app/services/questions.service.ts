
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Knowledgebase } from '../models/knowledgebase';
import { Observable } from 'rxjs';
import { Questions } from '../models/questions'
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class QuestionsService {

  constructor(private http: Http) { }

  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN});

  getQuestions(checklistType: number) {
    return this.http.get(environment.API_ENDPOINT + `/questions/items/${checklistType}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  newSprint(questions: Questions[], checklist_type: number): Observable<Questions[]> {
    return this.http
      .put(environment.API_ENDPOINT + `/questions/store/${checklist_type}`, JSON.stringify({ questions }),
      { headers: this.postHeaders }).pipe(
      map(response => {
        return response.json()
      }));
  }

  updateQuestions(id: number, questions: Questions[]) {
    return this.http.put(environment.API_ENDPOINT + `/questions/update/${id}`, JSON.stringify({ questions }),
      { headers: this.postHeaders }).pipe(
      map(response => response.json()))
  }

  newQuestion(checklist_type: number, questionName: string, ) {
    return this.http
      .put(environment.API_ENDPOINT + '/questions/item/new', JSON.stringify({ question: questionName, checklist_type: checklist_type }),
      { headers: this.postHeaders }).pipe(
      map(response => { return response.json() }));
  }

  updateQuestion(checklist_type: number, questionName: string, questionID: number) {
    return this.http
      .put(environment.API_ENDPOINT + `/questions/item/update/${questionID}`, JSON.stringify({ question: questionName, checklist_type: checklist_type}),
      { headers: this.postHeaders }).pipe(
      map(response => { return response.json() }));
  }

  deleteQuestion(id: number) {
    const url = environment.API_ENDPOINT + `/questions/item/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
        data => data,
        error => console.log('failed to delete checklist item')))
  }

  getChecklistItemsOnQuestionID(questionID: number) {
    return this.http.get(environment.API_ENDPOINT + `/checklist/item/question_sprint/${questionID}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

}
