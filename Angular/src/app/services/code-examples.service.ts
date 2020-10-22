
import { map } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { CodeExample } from '../models/code-example'
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class CodeExamplesService {

  constructor(private http: Http, private router: Router) { }
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getCode(category_id: number): Observable<CodeExample[]> {
    return this.http.get(environment.API_ENDPOINT + `/code/items/${category_id}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  getCodeExample(id:number): Observable<CodeExample[]> {
    return this.http.get(environment.API_ENDPOINT + `/code/${id}`, { headers: this.postHeaders }).pipe(
      map(response => response.json()))
  }

  newCodeExample(category_id:number, code: CodeExample): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + `/code/new/${category_id}`, JSON.stringify({
        title: code['title'],
        content: code['content'],
        code_lang: code['code_lang']
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  updateCodeExample(id: number, code: CodeExample): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + `/code/update/${id}`, JSON.stringify({
        title: code['title'],
        content: code['content'],
        code_lang: code['code_lang']
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  deleteCodeExample(id: number) {
    const url = environment.API_ENDPOINT + `/code/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
      data => data,
      error => console.log("failed to delete")))
  }
}