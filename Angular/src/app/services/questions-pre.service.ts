import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Question_pre } from '../models/question_pre';
import { Observable } from 'rxjs/Rx';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class QuestionPreService {

  constructor(private http: Http) { }
  
  public postHeaders = new Headers({'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });

  getPreQuestions(){
      return this.http.get("http://127.0.0.1:8888/api/questions_pre/items")
        .map(response => response.json().items)
  }


  newProject(questions:Question_pre[]): Observable<Question_pre[]> {
    return this.http
      .put('http://127.0.0.1:8888/api/questions_pre/store', JSON.stringify({questions}),
      { headers: this.postHeaders })
      .map(a => {return a.json()});
  }

}