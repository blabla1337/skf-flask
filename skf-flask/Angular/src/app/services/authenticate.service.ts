
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

  authenticate(user:User): Observable<any> {
    return this.http
      .post(environment.API_ENDPOINT + '/user/login', JSON.stringify({ userName: user['userName'], password: user['password'] }), { headers: this.headers }).pipe(
      map(response => {return response.json()}))
  }

  activateUser(user:User): Observable<string> {
    return this.http
      .put(environment.API_ENDPOINT + '/user/activate/' + user['user_id'], JSON.stringify({
        accessToken: parseInt(user['accessToken'], 10),
        email: user['email'],
        password: user['password'],
        repassword: user['repassword'],
        userName: user['userName']
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
