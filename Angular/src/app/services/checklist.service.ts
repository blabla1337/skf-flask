import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Checklist } from '../models/checklist';
import { Observable } from 'rxjs/Rx';

@Injectable()
export class ChecklistService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json'});
 
  getChecklist(id: number): Observable<Checklist[]> {
    return this.http.get(`http://127.0.0.1:8888/api/checklist/level/${id}`, { headers: this.headers })
      .map(response => response.json().items)
  }

}