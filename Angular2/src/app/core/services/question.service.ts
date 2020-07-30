import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root'
})

export class QuestionService
{
    constructor(
        private http: HttpClient,
    ) { }

    public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

    getQuestionCollection(id: number)
    {
        return this.http.get(environment.API_ENDPOINT + `/api/questions/items/${id}`)
    }


    storeSprintQuestions(checklist_type: number, maturity: number, questions: any[])
    {
        return this.http
            .put(environment.API_ENDPOINT + `/api/questions/store/${checklist_type}/${maturity}`, JSON.stringify({ questions }),
                { headers: this.authHeader })
    }
}