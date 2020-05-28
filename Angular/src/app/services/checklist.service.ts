import { map } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Checklist } from '../models/checklist';
import { ChecklistType } from '../models/checklist_type';
import { Observable } from 'rxjs';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';


@Injectable()
export class ChecklistService
{

  constructor(private http: Http) { }
  public checklist: Checklist;
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getChecklist(id: number, checklist_type: number): Observable<Checklist[]>
  {
    return this.http.get(environment.API_ENDPOINT + `/checklist/level/${id}/type/${checklist_type}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  getSingleChecklistItem(checklist_id: string, checklist_type: number): Observable<Checklist[]>
  {
    return this.http.get(environment.API_ENDPOINT + `/checklist/item/${checklist_id}/type/${checklist_type}`, { headers: this.postHeaders }).pipe(
      map(
        response => response.json(),
        () => console.log('failed to get the information')))
  }

  getChecklistByType(checklist_type: number): Observable<Checklist[]>
  {
    return this.http.get(environment.API_ENDPOINT + `/checklist/items/${checklist_type}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  getChecklistTypeList(category_id: number): Observable<ChecklistType[]>
  {
    return this.http.get(environment.API_ENDPOINT + `/checklist/types/${category_id}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  deleteChecklistType(id: number)
  {
    const url = environment.API_ENDPOINT + `/checklist/delete/type/${id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
        data => data,
        () => console.log('failed to delete checklist type')))
  }

  newChecklistType(category_id: number, checklistType: ChecklistType): Observable<any>
  {
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/create/type/${category_id}`, JSON.stringify({
        name: checklistType['name'],
        description: checklistType['description'],
        visibility: Number(checklistType['visibility'])
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  updateChecklistType(id: number, checklistType: ChecklistType): Observable<any>
  {
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/update/type/${id}`, JSON.stringify({
        name: checklistType['name'],
        description: checklistType['description'],
        visibility: Number(checklistType['visibility'])
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  newChecklistItem(checklistType: number, checklist: Checklist): Observable<any>
  {
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/new/item/${checklist['checklist_id']}/type/${checklistType}`, JSON.stringify({
        content: checklist['content'],
        kb_id: Number(checklist['kb_id']['kb_id']),
        include_always: checklist['include_always'],
        question_id: Number(checklist['question_id']['id']),
        cwe: Number(checklist['cwe']),
        maturity: Number(checklist['maturity'])
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  updateChecklistItem(checklist_id: string, checklistType: number, checklist: Checklist): Observable<any>
  {
    console.log(this.checklist)
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/update/item/${checklist_id}/type/${checklistType}`, JSON.stringify({
        content: checklist['content'],
        kb_id: Number(checklist['kb_id']['kb_id']),
        include_always: checklist['include_always'],
        question_id: Number(checklist['question_id']['id']),
        cwe: Number(checklist['cwe']),
        maturity: Number(checklist['maturity'])
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  updateChecklistItemCorraltion(checklist_id: string, checklistType: number, question_id: number): Observable<any>
  {
    console.log(this.checklist)
    return this.http
      .put(environment.API_ENDPOINT + `/checklist/update/item/correlation/${checklist_id}/type/${checklistType}`, JSON.stringify({
        question_id: Number(question_id),
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  deletechecklistItem(checklist_id: string, checklistType: number)
  {
    const url = environment.API_ENDPOINT + `/checklist/delete/item/${checklist_id}/type/${checklistType}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
        data => data,
        error => console.log('failed to delete checklist item')))
  }


}
