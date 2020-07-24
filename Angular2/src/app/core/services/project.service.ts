
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class ProjectService
{
    public category_id: number;

    constructor(
        private http: HttpClient,
    ) { }

    public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

    getProjectsCollection(): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/project/items`, { headers: this.authHeader })
    }

    getProjectItem(id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/project/item/${id}`, { headers: this.authHeader })
    }

    createProject(value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/project/new`, value, { headers: this.authHeader })
    }

    updateProject(id: number, value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/project/update/${id}`, value, { headers: this.authHeader })
    }

    deleteProject(id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/project/delete/${id}`, { headers: this.authHeader })
    }

}