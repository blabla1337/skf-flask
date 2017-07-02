import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { User } from '../models/user'
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';


@Injectable()
export class AuthenticateService {
  public loggedIn: boolean;
  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });

  authenticate(username: string, password: string) {
    return this.http
      .post(environment.API_ENDPOINT + '/user/login', JSON.stringify({ username: username, password: password }), { headers: this.headers })
      .map(response => response.json()).map(response => {
        if (response["Authorization token"] != "") {
          sessionStorage.setItem("auth_token", response["Authorization token"]);
          sessionStorage.setItem("user", response["username"]);
          location.replace("dashboard"),
           error => console.log("An error occured whilst logging in");
        }
      })
  }

  activateUser(email: string, username: string, accessToken: string, password: string, repassword: string, userID: number): Observable<User[]> {
    return this.http
      .put(environment.API_ENDPOINT + '/user/activate/' + userID, JSON.stringify({
        accessToken: parseInt(accessToken, 10),
        email: email,
        password: password,
        repassword: repassword,
        username: username
      }),
      { headers: this.headers })
      .map(response => {
        return response.json()
      });
  }

  logout() {
    AppSettings.AUTH_TOKEN = null;
    this.loggedIn = false;
  }

  isLoggedIn() {
    return this.loggedIn;
  }
}