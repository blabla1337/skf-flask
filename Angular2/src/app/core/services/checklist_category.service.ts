import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})

export class ChecklistCategoryService
{
    constructor(
        private http: HttpClient,
    ) { }

    getChecklistCategoryCollection()
    {
        return this.http.get('https://beta.securityknowledgeframework.org/api/checklist_category/items')
    }
}