
import { map } from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Observable } from 'rxjs';
import { Sprint } from '../models/sprint';
import { AppSettings } from '../globals';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class SprintService
{

  constructor(
    private http: Http,
  ) { }


  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  newSprint(name: string, project_id: number, description: string): Observable<Sprint>
  {
    return this.http
      .put(environment.API_ENDPOINT + '/sprint/new', JSON.stringify({
        name: name,
        description: description,
        project_id: project_id
      }),
        { headers: this.postHeaders }).pipe(
          map(a => { return a.json() }));
  }

  getSprintStats(project_id: number): Observable<Sprint[]>
  {
    return this.http.get(environment.API_ENDPOINT + `/sprint/stats/${project_id}`, { headers: this.postHeaders }).pipe(
      map(response => response.json()))
  }

  getSprintResults(sprint_id: number): Observable<Sprint[]>
  {
    return this.http.get(environment.API_ENDPOINT + `/sprint/results/${sprint_id}`, { headers: this.postHeaders }).pipe(
      map(response => response.json().items))
  }

  getSprintResultsExport(sprint_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/sprint/results/export/${sprint_id}`, { headers: this.postHeaders }).pipe(
      map(
        response => response.json().message,
        () => console.log('failed to export')));
  }

  getSprintResultsExportExternal(id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/sprint/results/export_external/${id}`, { headers: this.postHeaders }).pipe(
      map(
        response => response.json().message,
        () => console.log('failed to export')));
  }

  delete(sprint_id: number)
  {
    const url = environment.API_ENDPOINT + `/sprint/delete/${sprint_id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
        data => data,
        () => console.log('failed to delete')))
  }

  deleteChecklistResult(checklist_result_id: number)
  {
    const url = environment.API_ENDPOINT + `/sprint/results/delete/${checklist_result_id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
        data => data,
        () => console.log('failed to delete')))
  }

  updateChecklistResult(checklist_result_id: number, sprint: Sprint)
  {
    return this.http
      .put(environment.API_ENDPOINT + `/sprint/results/update/${checklist_result_id}`, JSON.stringify({
        evidence: sprint['evidence'],
        resolved: sprint['resolved']
      }),
        { headers: this.postHeaders }).pipe(
          map(response => { return response.json() }));
  }

}
