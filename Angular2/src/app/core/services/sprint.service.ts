
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

    public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

    getSprintsCollection(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/stats/${id}`, { headers: this.headers })
    }

    getSprintChecklistResults(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/results/${id}`, { headers: this.headers })
    }

    createSprint(value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/sprint/new`, value, { headers: this.headers })
    }

    deleteSprint(id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/project/delete/${id}`, { headers: this.headers })
    }

    deleteChecklistResultFromSprint(id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/project/delete/${id}`, { headers: this.headers })
    }

    getCompliance(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/results/update/${id}`, { headers: this.headers })
    }

    updateCompliance(id: number, value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/sprint/results/update/${id}`, value, { headers: this.headers })
    }

    exportCsv(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/sprint/results/export/${id}`, { headers: this.headers })
    }

    deleteControlsFromSprint(id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/sprint/results/delete/${id}`, { headers: this.headers })
    }
}