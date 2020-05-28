
import { map } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Labs } from '../models/labs';
import { AppSettings } from '../globals';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class LabService
{

  constructor(private http: Http) { }
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getLabs(): Observable<Labs[]>
  {
    return this.http.get(environment.API_ENDPOINT + '/interactive_labs/items', { headers: this.postHeaders }).pipe(
      map(response => response.json().items));
  }


  deployLab(image_tag)
  {
    return this.http.get(environment.API_ENDPOINT + `/interactive_labs/deployments/${image_tag}`, { headers: this.postHeaders }).pipe(
      map(response => response.json()));
  }


  deleteLab(image_tag)
  {
    return this.http.get(environment.API_ENDPOINT + `/interactive_labs/delete-deployments/${image_tag}`, { headers: this.postHeaders }).pipe(
      map(response => response.json()));
  }
}
