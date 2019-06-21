
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { User } from '../models/user'
import { Observable } from 'rxjs';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';


@Injectable()
export class AuthenticateService {
  public loggedIn: boolean;
  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });

  authenticate(username: string, password: string): Observable<any> {
    return this.http
      .post(environment.API_ENDPOINT + '/user/login', JSON.stringify({ username: username, password: password }), { headers: this.headers }).pipe(
      map(response => {return response.json()}))
  }

  activateUser(email: string, username: string, accessToken: string, password: string, repassword: string, userID: number): Observable<string> {
    return this.http
      .put(environment.API_ENDPOINT + '/user/activate/' + userID, JSON.stringify({
        accessToken: parseInt(accessToken, 10),
        email: email,
        password: password,
        repassword: repassword,
        username: username
      }),
      { headers: this.headers }).pipe(
      map(response => { return response.json()}));
  }

  logout() {
    AppSettings.AUTH_TOKEN = null;
    this.loggedIn = false;
  }

  isLoggedIn() {
    return this.loggedIn;
  }
}
