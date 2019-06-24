
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Knowledgebase } from '../models/knowledgebase';
import { AppSettings } from '../globals';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class KnowledgebaseService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getKnowledgeBase(): Observable<Knowledgebase[]> {
    return this.http.get(environment.API_ENDPOINT + '/kb/items', { headers: this.headers }).pipe(
      map(response => response.json().items));
  }

  getKnowledgebaseItem(id: number): Observable<Knowledgebase[]> {
    return this.http.get(environment.API_ENDPOINT + `/kb/${id}`, { headers: this.headers }).pipe(
      map(response => response.json()));
  }

  newKnowledgebaseItem(title: string,  content: string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/kb/new', JSON.stringify({
        title: title,
        content: content
      }),
      { headers: this.postHeaders }).pipe(
      map(a => { return a.json() }));
  }

  updateKnowledgebaseItem(id: number , title: string,  content: string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + `/kb/update/${id}`, JSON.stringify({
        title: title,
        content: content
      }),
      { headers: this.postHeaders }).pipe(
      map(a => { return a.json() }));
  }

  deleteKnowledgebaseItem(id: number) {
    const url = environment.API_ENDPOINT + `/kb/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
      data => data,
      error => console.log('failed to delete')))
  }




}
