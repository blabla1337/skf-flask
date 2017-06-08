import { Injectable } from '@angular/core';
import { CodeExample } from '../models/code-example'
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class CodeExamplesService {

  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });
  
  getCode(codeLang: string): Observable<CodeExample[]> {
    if (codeLang) {
      localStorage.setItem("code_lang", codeLang);
    }
    
    if(localStorage.getItem("code_lang") === null){
      localStorage.setItem("code_lang", "php");
    }

   return this.http.get('http://127.0.0.1:8888/api/code/lang/'+codeLang, { headers: this.headers })
      .map(response => response.json().items)
  }
}