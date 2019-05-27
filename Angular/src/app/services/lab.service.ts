import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Labs } from '../models/labs';
import { AppSettings } from '../globals';
import { Observable } from 'rxjs/Rx';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class LabService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getLabs(): Observable<Labs[]> {
    return this.http.get(environment.API_ENDPOINT + '/interactive_labs/items', { headers: this.headers })
      .map(response => response.json().items);
  }
}