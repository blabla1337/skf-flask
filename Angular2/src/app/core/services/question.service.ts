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

    getQuestionCollection(checklist_id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/questions/items/${checklist_id}`, { headers: this.authHeader })
    }

    newQuestionItem(value: any)
    {
        return this.http.put(environment.API_ENDPOINT + `/api/questions/item/new`, value, { headers: this.authHeader })
    }

    getQuestionById(question_id: number)
    {
        return this.http.get(environment.API_ENDPOINT + `/api/questions/item/${question_id}`, { headers: this.authHeader })
    }

    deleteQuestionById(question_id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/questions/item/delete/${question_id}`, { headers: this.authHeader })
    }

    updateQuestion(value: any, question_id: number)
    {
        return this.http.put(environment.API_ENDPOINT + `/api/questions/item/update/${question_id}`, value, { headers: this.authHeader })
    }

    storeSprintQuestions(checklist_type: number, maturity: number, questions: any[]): Observable<Object>
    {
        return this.http
            .put(environment.API_ENDPOINT + `/api/questions/store/${checklist_type}/${maturity}`, JSON.stringify({ questions }),
                { headers: this.authHeader })
    }
}