
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Comment } from '../models/comment';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class CommentService {

  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Authorization': AppSettings.AUTH_TOKEN });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  newComment(checklistID: string, comment: string, sprintName: string, status: number, projectID: number): Observable<Comment> {
    return this.http
      .put(environment.API_ENDPOINT + '/comment/new', JSON.stringify({
        checklistID: checklistID,
        comment: comment,
        sprintName: sprintName,
        status: status,
        projectID: projectID
      }),
      { headers: this.postHeaders }).pipe(
      map(a => { return a.json() }));
  }

  getComment(checklistID: string, sprintName: string): Observable<Comment> {
    return this.http
      .post(environment.API_ENDPOINT + '/comment/items', JSON.stringify({
        checklistID: checklistID,
        sprintName: sprintName
      }),
      { headers: this.postHeaders }).pipe(
      map(a => { return a.json().items }));
  }
}
