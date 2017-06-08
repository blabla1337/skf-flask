import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Project } from '../models/project';
import 'rxjs/add/operator/toPromise';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class ProjectService {

  constructor(private http: Http, private router: Router) { }
  
  public postHeaders = new Headers({'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });
  public getHeaders = new Headers({'Authorization': sessionStorage.getItem('auth_token') });

  newProject(name: string, version: string, description: string): Observable<any> {
    return this.http
      .put('http://127.0.0.1:8888/api/project/new', JSON.stringify({
        name: name,
        version: version,
        description: description,
        level:1
      }),
      { headers: this.postHeaders })
      .map(a => {return a.json()});
  }

  getProjects(): Observable<Project[]> {
    return this.http.get("http://127.0.0.1:8888/api/project/items", { headers: this.getHeaders })
      .map(response => response.json().items)
  }

  delete(id: number) {
    const url = `http://127.0.0.1:8888/api/project/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders })
      .map(
      data => data,
      error => console.log("failed to delete"))
  }
}