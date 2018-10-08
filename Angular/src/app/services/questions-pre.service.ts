import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Question_pre } from '../models/question_pre';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class QuestionPreService {

  constructor(private http: Http) { }

  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getPreQuestions(checklistType:number) {
    return this.http.get(environment.API_ENDPOINT + `/questions_pre/items/${checklistType}`, { headers: this.postHeaders })
      .map(response => response.json().items)
  }

  newProject(questions: Question_pre[]): Observable<Question_pre[]> {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_pre/store', JSON.stringify({ questions }),
      { headers: this.postHeaders })
      .map(response => { return response.json() });
  }

  updatePre(id: number, questions: Question_pre[]) {
    return this.http.put(environment.API_ENDPOINT + `/questions_pre/update/${id}`, JSON.stringify({ questions }),
      { headers: this.postHeaders })
      .map(response => response.json())
  }

  newQuestion(checklist_type:string, questionName:string, ) {
    return this.http
      .put(environment.API_ENDPOINT + '/questions_pre/item/new', JSON.stringify({ question:questionName, checklist_type:checklist_type }),
      { headers: this.postHeaders })
      .map(response => { return response.json() });
  }

  updateQuestion(checklist_type:string, questionName:string, questionID:number) {
    return this.http
      .put(environment.API_ENDPOINT + `/questions_pre/item/update/${questionID}`, JSON.stringify({ question:questionName, checklist_type:checklist_type}),
      { headers: this.postHeaders })
      .map(response => { return response.json() });
  }

  deleteQuestion(id: number) {
    const url = environment.API_ENDPOINT + `/questions_pre/item/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders })
      .map(
        data => data,
        error => console.log("failed to delete checklist item"))
  }

}