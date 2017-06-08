import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Comment } from '../models/comment';
import 'rxjs/add/operator/toPromise';
import { Router } from '@angular/router';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class CommentService {

  constructor(private http: Http, private router: Router) { }
  public headers = new Headers({ 'Authorization': sessionStorage.getItem('auth_token') });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem('auth_token') });
 
  newComment(checklistID: string, comment: string, sprintID: string, status: number): Observable<Comment> {
    return this.http
      .put('http://127.0.0.1:8888/api/comment/new', JSON.stringify({
        checklistID: checklistID,
        comment: comment,
        sprintID: parseInt(sprintID, 10),
        status:status
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

   getComment(checklistID: string, sprintID: string): Observable<Comment> {
    return this.http
      .post('http://127.0.0.1:8888/api/comment/items', JSON.stringify({
        checklistID: checklistID,
        sprintID: parseInt(sprintID, 10)
      }),
      { headers: this.postHeaders })
      .map(a => { return a.json().items});
  }
}
