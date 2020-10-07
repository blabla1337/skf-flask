
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class SprintService
{
    public category_id: number;

    constructor(
        private http: HttpClient,
    ) { }

    public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

    getSprintsCollection(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/stats/${id}`, { headers: this.authHeader })
    }

    getSprintChecklistResults(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/results/${id}`, { headers: this.authHeader })
    }

    createSprint(value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/sprint/new`, value, { headers: this.authHeader })
    }

    deleteSprint(id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/project/delete/${id}`, { headers: this.authHeader })
    }

    deleteChecklistResultFromSprint(id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/project/delete/${id}`, { headers: this.authHeader })
    }

    getCompliance(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/results/update/${id}`, { headers: this.authHeader })
    }

    updateCompliance(id: number, value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/sprint/results/update/${id}`, value, { headers: this.authHeader })
    }

    exportCsv(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/results/export/${id}`, { headers: this.authHeader })
    }
}