import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

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
        return this.http.get(environment.API_ENDPOINT + '/api/checklist_category/items');
    }
}
