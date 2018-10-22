import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Checklist } from '../models/checklist';
import { ChecklistType } from '../models/checklist_type';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';


@Injectable()
export class ChecklistService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getChecklist(id: number, checklist_type: number): Observable<Checklist[]> {
    return this.http.get(environment.API_ENDPOINT + `/checklist/level/${id}/type/${checklist_type}`, { headers: this.headers })
      .map(response => response.json().items)
  }

  getChecklistByType(checklist_type: number): Observable<Checklist[]> {
    return this.http.get(environment.API_ENDPOINT + `/checklist/items/${checklist_type}`, { headers: this.headers })
      .map(response => response.json().items)
  }

  getChecklistTypeList(): Observable<ChecklistType[]> {
    return this.http.get(environment.API_ENDPOINT + `/checklist/types`, { headers: this.headers })
      .map(response => response.json().items)
  }

  deletechecklistType(id: number) {
    const url = environment.API_ENDPOINT + `/checklist/delete/type/${id}`;
    return this.http.delete(url, { headers: this.postHeaders })
      .map(
        data => data,
        error => console.log("failed to delete checklist type"))
  }

  newChecklistTyoe(checklist_name: string, checklist_description:string): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/checklist/create/type', JSON.stringify({
        checklist_name: checklist_name,
        checklist_description: checklist_description
      }),
        { headers: this.postHeaders })
      .map(a => { return a.json() });
  }
  
  newChecklistItem(checklistType: number, checklistID:number ,content:string, kbID:number, include_always:string, include_first:string, question_sprint_ID:number, question_pre_ID:number): Observable<any> {
    console.log()
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/new/item/${checklistID}/type/${checklistType}`, JSON.stringify({
       content: content,
       kbID:kbID,
       include_always:include_always,
       include_first:include_first,
       question_sprint_ID:question_sprint_ID,
       question_pre_ID:question_pre_ID,
      }),
        { headers: this.postHeaders })
      .map(a => { return a.json() });
  }

  deletechecklistItem(id: string) {
    const url = environment.API_ENDPOINT + `/checklist/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders })
      .map(
        data => data,
        error => console.log("failed to delete checklist item"))
  }

  updateChecklistItem(checklistType: number, checklistID:number ,content:string, kbID:number, include_always:string, include_first:string, question_sprint_ID:number, question_pre_ID:number): Observable<any> {
    
    console.log(include_always)
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/update/item/${checklistID}/type/${checklistType}`, JSON.stringify({
       content: content,
       kbID:kbID,
       include_always:include_always,
       include_first:include_first,
       question_sprint_ID:question_sprint_ID,
       question_pre_ID:question_pre_ID,
      }),
        { headers: this.postHeaders })
      .map(a => { return a.json() });
  }
  
}