
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class SearchService
{

  constructor(
    private http: HttpClient,
  ) { }

  public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

  searchChecklist(checklistName: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/search/checklist/${checklistName}`, { headers: this.headers })
  }

  searchKb(kbName: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/search/kb/${kbName}`, { headers: this.headers })
  }

  searchLabs(labName: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/search/lab/${labName}`, { headers: this.headers })
  }

  searchProject(projectName: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/search/project/${projectName}`, { headers: this.headers })
  }

  searchCode(codeName: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/search/code/${codeName}`, { headers: this.headers })
  }  
}