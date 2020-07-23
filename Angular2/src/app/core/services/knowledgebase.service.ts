
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class KnowledgebaseService
{
    public category_id: number;

    constructor(
        private http: HttpClient,
    ) { }

    public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

    getKnowledgeBaseItemsCollection(category_id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/kb/items/${category_id}`, { headers: this.authHeader })
    }

    getKnowledgeBaseItem(kb_id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/kb/${kb_id}`, { headers: this.authHeader })
    }

    createKnowledgebaseItem(value: any): Observable<Object>
    {
        this.category_id = Number(localStorage.getItem("categorySelector"))
        return this.http.put(environment.API_ENDPOINT + `/api/kb/new/${this.category_id}`, value, { headers: this.authHeader })
    }

    updateKnowledgebaseItem(kb_id: number, value: any): Observable<Object>
    {
        return this.http.put(environment.API_ENDPOINT + `/api/kb/update/${kb_id}`, value, { headers: this.authHeader })
    }

    deleteknowledgebaseItem(kb_id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/kb/delete/${kb_id}`, { headers: this.authHeader })
    }

}