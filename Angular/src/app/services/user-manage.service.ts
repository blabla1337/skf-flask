import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { User } from '../models/user';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';

@Injectable()
export class UserService {

  constructor(private http: Http, private router: Router) { }
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });
  public getHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getUsers(): Observable<User[]> {
    return this.http.get(environment.API_ENDPOINT + '/user/list', { headers: this.getHeaders })
      .map(response => response.json().items)
  }

  revoke(id: number) {
    const url = environment.API_ENDPOINT + ``;
    return this.http
      .put(environment.API_ENDPOINT + `/user/manage/${id}`, JSON.stringify({
        active: "False"
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

  grant(id: number) {
    const url = environment.API_ENDPOINT + ``;
    return this.http
      .put(environment.API_ENDPOINT + `/user/manage/${id}`, JSON.stringify({
        active: "True"
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }
}