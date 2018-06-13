import { Injectable } from '@angular/core';
import { CodeExample } from '../models/code-example'
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class CodeExamplesService {

  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getCode(codeLang: string): Observable<CodeExample[]> {
    if (codeLang) {
      localStorage.setItem("code_lang", codeLang);
    }

    if (localStorage.getItem("code_lang") === null) {
      localStorage.setItem("code_lang", "php");
    }

    return this.http.get(environment.API_ENDPOINT + '/code/lang/' + codeLang, { headers: this.headers })
      .map(response => response.json().items)
  }
}