import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Auth } from '../models/auth.model';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private http: HttpClient,
) { }

public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

addUser(user: Auth) {
  let users = [];
  if (localStorage.getItem('Users')) {
    users = JSON.parse(localStorage.getItem('Users'));
    users = [user, ...users];
  } else {
    users = [user];
  }
  localStorage.setItem('Users', JSON.stringify(users));
}

activateUser(value: any, user_id: number): Observable<Object> {
    return this.http.put(environment.API_ENDPOINT + `/user/activate/${user_id}`, value, { headers: this.authHeader })
}

}
