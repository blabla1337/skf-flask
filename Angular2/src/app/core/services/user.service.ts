import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

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

  activateUser(value: any, user_id: number): Observable<Object> {
      return this.http.put(environment.API_ENDPOINT + `/api/user/activate/${user_id}`, value, { headers: this.authHeader })
  }

  createUser(value: any): Observable<Object> {
    return this.http.put(environment.API_ENDPOINT + `/api/user/create`, value, { headers: this.authHeader })
  }

  getUsers(): Observable<Object> {
    return this.http.get(environment.API_ENDPOINT + `/api/user/list`, { headers: this.authHeader })
  }

  accessUser(value: any, user_id: number): Observable<Object> {
    return this.http.put(environment.API_ENDPOINT + `/api/user/manage/${user_id}`, value, { headers: this.authHeader })
  }

}
