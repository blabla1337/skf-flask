import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';
import jwt_decode from 'jwt-decode';

@Injectable({
  providedIn: 'root'
})
export class UserService
{

  constructor(
    private http: HttpClient,
  ) { }

  public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

  getJwtUserId(): string | undefined {
    try {
      const jwtToken = sessionStorage.getItem("access_token");
      if (jwtToken === undefined || jwtToken === "") {
        return undefined;
      }
      const decodedJWT: any = jwt_decode(jwtToken);
      return decodedJWT.sub;
    } catch(e) {
      console.error("jwt_decode error: ", e);
      return undefined;
    }
  }

  activateUser(value: any, user_id: number): Observable<Object>
  {
    return this.http.put(environment.API_ENDPOINT + `/api/user/activate/${user_id}`, value, { headers: this.headers })
  }

  createUser(value: any): Observable<Object>
  {
    return this.http.put(environment.API_ENDPOINT + `/api/user/create`, value, { headers: this.headers })
  }

  getUsers(): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/user/list`, { headers: this.headers })
  }

  accessUser(value: any, user_id: number): Observable<Object>
  {
    return this.http.put(environment.API_ENDPOINT + `/api/user/manage/${user_id}`, value, { headers: this.headers })
  }

  getPrivileges()
  {
    return this.http.get(environment.API_ENDPOINT + `/api/user/list_privileges`, { headers: this.headers })
  }

}
