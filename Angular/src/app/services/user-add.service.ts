import { Injectable } from '@angular/core';
import { User } from '../models/user'
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';

@Injectable()
export class UserAddService {

  constructor(private http: Http, private router: Router) { }
   public headers = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  newUser(email: string, privileges: string): Observable<User[]> {
   
    return this.http
      .put(AppSettings.API_ENDPOINT + '/user/create', JSON.stringify({
        email: email,
        privilege: parseInt(privileges, 10)
      }),
      { headers: this.headers })
      .map(res => res.json() as User[])
  }
}