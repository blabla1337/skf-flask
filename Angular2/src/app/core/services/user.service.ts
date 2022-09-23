import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { v4 as uuidv4 } from 'uuid';
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

  getJwtUserId() {
    try {
      const jwtToken = sessionStorage.getItem("access_token");
      if(environment.AUTH_METHOD == "skiploginprovider"){
        if (jwtToken === undefined || jwtToken === "" || jwtToken === null ) {
          sessionStorage.setItem("user_id",uuidv4());
          return
        }
      }
      const decodedJWT: any = jwt_decode(jwtToken);
      sessionStorage.setItem("user_id",decodedJWT.sub);
      return
    } catch(e) {
      console.error("jwt_decode error: ", e);
      return
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

  getActive()
  {
    return this.http.get(environment.API_ENDPOINT + `/api/kb/1`, { headers: this.headers, observe: "response" })
  }
}
