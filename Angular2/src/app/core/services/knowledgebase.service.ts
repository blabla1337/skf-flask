
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class KnowledgebaseService
{

    constructor(
        private http: HttpClient,
    ) { }

    getKnowledgeBaseItems(category_id: number)
    {
        return this.http.get(`http://localhost:8888/api/kb/items/${category_id}`)
    }

}