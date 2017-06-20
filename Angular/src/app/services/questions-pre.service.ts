import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Question_pre } from '../models/question_pre';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';


@Injectable()
export class QuestionPreService {

  constructor(private http: Http) { }

  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getPreQuestions() {
    return this.http.get(AppSettings.API_ENDPOINT + '/questions_pre/items')
      .map(response => response.json().items)
  }

  newProject(questions: Question_pre[]): Observable<Question_pre[]> {
    return this.http
      .put(AppSettings.API_ENDPOINT + '/questions_pre/store', JSON.stringify({ questions }),
      { headers: this.postHeaders })
      .map(response => { return response.json() });
  }

  updatePre(id: number, questions: Question_pre[]) {
    return this.http.put(AppSettings.API_ENDPOINT + `/questions_pre/update/${id}`, JSON.stringify({ questions }),
      { headers: this.postHeaders })
      .map(response => response.json())
  }

}