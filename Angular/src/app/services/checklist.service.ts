import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Checklist } from '../models/checklist';
import { Observable } from 'rxjs/Rx';
import { Question_post } from '../models/question_post'

@Injectable()
export class ChecklistService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json'});
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });

  getChecklist(id: number): Observable<Checklist[]> {
    return this.http.get(`http://127.0.0.1:8888/api/checklist/level/${id}`, { headers: this.headers })
      .map(response => response.json().items)
  }

    newChecklist(questions:Question_post[]): Observable<Question_post[]> {  
    return this.http
      .put('http://127.0.0.1:8888/api/questions_post/store', JSON.stringify({questions}),
      { headers: this.postHeaders })
      .map(a => { 
        return a.json()});
  }

}