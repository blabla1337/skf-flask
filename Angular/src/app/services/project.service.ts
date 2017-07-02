import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Project } from '../models/project';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';

@Injectable()
export class ProjectService {

  constructor(private http: Http, private router: Router) { }
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });
  public getHeaders = new Headers({ 'Authorization': AppSettings.AUTH_TOKEN });

  newProject(name: string, version: string, description: string, level: string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/project/new', JSON.stringify({
        name: name,
        version: version,
        description: description,
        level: parseInt(level, 10)
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

  getProjects(): Observable<Project[]> {
    return this.http.get(environment.API_ENDPOINT + '/project/items', { headers: this.getHeaders })
      .map(response => response.json().items)
  }

  delete(id: number) {
    const url = environment.API_ENDPOINT + `/project/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders })
      .map(
      data => data,
      error => console.log("failed to delete"))
  }
}