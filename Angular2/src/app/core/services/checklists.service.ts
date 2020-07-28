
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class ChecklistService
{

  constructor(
    private http: HttpClient,
  ) { }

  public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

  getChecklistsCollection(id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist/types/${id}`, { headers: this.authHeader })
  }
}