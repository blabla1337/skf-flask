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
        return this.http.get('http://localhost:8888/api/checklist_category/items')
    }
}