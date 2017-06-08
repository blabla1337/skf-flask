import { Injectable } from '@angular/core';
import { User } from '../models/user'
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class UserAddService {

  constructor(private http: Http, private router: Router) { }

  newUser(email: string, privileges: string): Observable<User[]> {
    let headers = new Headers({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });

    return this.http
      .put('http://127.0.0.1:8888/api/user/create', JSON.stringify({
        email: email,
        privilege: parseInt(privileges, 10)
      }),
      { headers: headers })
      .map(res => res.json() as User[])
  }
}