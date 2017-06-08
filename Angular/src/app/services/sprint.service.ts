import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Sprint } from '../models/sprint';
import 'rxjs/add/operator/toPromise';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class SprintService {

  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Authorization': sessionStorage.getItem('auth_token') });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });
 
  newSprint(name: string, projectID: number, description: string): Observable<Sprint> {
    return this.http
      .put('http://127.0.0.1:8888/api/sprint/new', JSON.stringify({
        name: name,
        description: description,
        projectID: projectID
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

  getSprintStats(id: number): Observable<Sprint[]> {
    return this.http.get(`http://127.0.0.1:8888/api/sprint/stats/${id}`, { headers: this.headers })
      .map(response => response.json())
  }

    getSprintResults(id: number): Observable<Sprint[]> {
    return this.http.get(`http://127.0.0.1:8888/api/sprint/results/${id}`, { headers: this.headers })
      .map(response => response.json().items)
  }

  delete(id: number) {
    const url = `http://127.0.0.1:8888/api/sprint/delete/${id}`;
    return this.http.delete(url, { headers: this.headers })
      .map(
      data => data,
      error => console.log("failed to delete"))
  }
}