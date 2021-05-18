
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})

export class LabService
{

  constructor(
    private http: HttpClient,
  ) { }

  public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

  getLabs(): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + '/api/interactive_labs/items')
  }

  deployLab(image_tag: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/interactive_labs/deployments/${image_tag}`, { headers: this.authHeader })
  }

  deleteLab(image_tag: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/interactive_labs/delete-deployments/${image_tag}`, { headers: this.authHeader })
  }

  getCodeLabs(code_type: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/code_review_labs/challenge/${code_type}`, { headers: this.authHeader })
  }


  solveCodeReviewChallenge(code_id: number, solution_id: number): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/code_review_labs/solve_challenge/${code_id}/solution/${solution_id}`, { headers: this.authHeader })
  }

}