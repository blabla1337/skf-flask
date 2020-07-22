
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
    providedIn: 'root'
})

export class LabService
{

    constructor(
        private http: HttpClient,
    ) { }

    getLabs()
    {
        return this.http.get(environment.API_ENDPOINT + '/api/interactive_labs/items')
    }

}