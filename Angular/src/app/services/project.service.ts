import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Project } from '../models/project';
import { ProjectStats } from '../models/project_stats';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class ProjectService {

  constructor(private http: Http, private router: Router) { }
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });
  public getHeaders = new Headers({ 'Authorization': AppSettings.AUTH_TOKEN });

  newProject(name: string,  description: string, checklist_type: number, version: string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/project/new', JSON.stringify({
        name: name,
        description: description,
        checklist_type: checklist_type,
        version: version
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

  getProjects(): Observable<Project[]> {
    return this.http.get(environment.API_ENDPOINT + '/project/items', { headers: this.getHeaders })
      .map(response => response.json().items)
  }

  getProject(id: number): Observable<Project[]> {
    return this.http.get(environment.API_ENDPOINT + `/project/${id}`, { headers: this.getHeaders })
      .map(response => response.json().items)
  }

  delete(id: number) {
    const url = environment.API_ENDPOINT + `/project/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders })
      .map(
      data => data,
      error => console.log("failed to delete"))
  }

  getStats(id: number): Observable<ProjectStats[]> {
    const url = environment.API_ENDPOINT + `/project/stats/${id}`;
    return this.http.get(url, { headers: this.getHeaders })
      .map(response => response.json().items)
  }
}