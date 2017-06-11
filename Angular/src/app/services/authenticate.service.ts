import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { User } from '../models/user'
import { Observable } from 'rxjs/Rx';

@Injectable()
export class AuthenticateService {
  public loggedIn: boolean;

  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });

  authenticate(username: string, password: string) {
    return this.http
      .post('http://127.0.0.1:8888/api/user/login', JSON.stringify({ username: username, password: password }), { headers: this.headers })
      .map(response => response.json()).map(response => {
        if (response["Authorization token"] != null && response["Authorization token"] != "Wrong username/password") {
          sessionStorage.setItem("auth_token", response["Authorization token"]);
          location.replace("dashboard"),
            error => console.log("An error occured whilst logging in");
        }
      })
  }

  activateUser(email:string, username:string, accessToken:string, password:string, repassword:string, userID:number): Observable<User[]> {
    return this.http
      .put('http://127.0.0.1:8888/api/user/activate/'+userID, JSON.stringify({
        accessToken: parseInt(accessToken,10),
        email:email,
        password:password,
        repassword:repassword,
        username:username
      }),
      { headers: this.headers })
      .map(response => {
        return response.json()
      });
  }


  logout() {
    sessionStorage.removeItem('auth_token');
    this.loggedIn = false;
  }

  isLoggedIn() {
    return this.loggedIn;
  }
}