import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService
{
  loggedinUser: string;
  loggedin = false;

  constructor(
    private http: HttpClient,
  ) { }

  public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': "null" });

  LoginSKFprovider(user: any)
  {
    return this.http.post(environment.API_ENDPOINT + `/api/user/login`, user, { headers: this.authHeader })
  }

  LoginSkipprovider()
  {
    return this.http.get(environment.API_ENDPOINT + `/api/user/skip`, { headers: this.authHeader })
  }

  loggedIn()
  {
    this.loggedinUser = sessionStorage.getItem('Authorization');
    if (this.loggedinUser) {
      return this.loggedin = true;
    } else {
      return this.loggedin = false;
    }
  }

}
