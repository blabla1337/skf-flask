import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
    providedIn: 'root'
})

export class QuestionService
{
    constructor(
        private http: HttpClient,
    ) { }

    getQuestionCollection(id: number)
    {
        return this.http.get(environment.API_ENDPOINT + `/api/questions/items/${id}`)
    }
}