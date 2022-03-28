
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

  public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

  getLabs(): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + '/api/interactive_labs/items', { headers: this.headers })
  }

  deployLab(image_id: string, user_id: string): Observable<Object>
  {
    return this.http.post(environment.API_ENDPOINT + `/api/interactive_labs/deployments/${image_id}`
      , {
      user_id
      }
      , { headers: this.headers })
  }

  deleteLab(image_id: number, user_id: string): Observable<Object>
  {
    return this.http.post(environment.API_ENDPOINT + `/api/interactive_labs/delete-deployments/${image_id}`
    , {
      user_id
      }
      , { headers: this.headers })
  }

  getCodeLabs(code_type: string): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/code_review_labs/challenge/${code_type}`, { headers: this.headers })
  }


  solveCodeReviewChallenge(code_id: number, solution_id: number): Observable<Object>
  {
    return this.http.get(environment.API_ENDPOINT + `/api/code_review_labs/solve_challenge/${code_id}/solution/${solution_id}`, { headers: this.headers })
  }

}
