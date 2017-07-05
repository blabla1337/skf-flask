import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';
import { Sprint } from '../models/sprint';
import { AppSettings } from '../globals';

@Injectable()
export class SprintService {

  constructor(
    private http: Http,
    private router: Router,
  ) { }

  public headers = new Headers({ 'Authorization': AppSettings.AUTH_TOKEN });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  newSprint(name: string, projectID: number, description: string): Observable<Sprint> {
    return this.http
      .put(AppSettings.API_ENDPOINT + '/sprint/new', JSON.stringify({
        name: name,
        description: description,
        projectID: projectID
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

  getSprintStats(id: number): Observable<Sprint[]> {
    return this.http.get(AppSettings.API_ENDPOINT + `/sprint/stats/${id}`, { headers: this.headers })
      .map(response => response.json())
  }

  getSprintResults(id: number): Observable<Sprint[]> {
    return this.http.get(AppSettings.API_ENDPOINT + `/sprint/results/${id}`, { headers: this.headers })
      .map(response => response.json().items)
  }

  getSprintResultsAudit(id: number): Observable<Sprint[]> {
    return this.http.get(AppSettings.API_ENDPOINT + `/sprint/results/audit/${id}`, { headers: this.headers })
      .map(response => response.json().items)
  }

  delete(id: number) {
    const url = AppSettings.API_ENDPOINT + `/sprint/delete/${id}`;
    return this.http.delete(url, { headers: this.headers })
      .map(
      data => data,
      error => console.log("failed to delete"))
  }
}