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

    public headers = new HttpHeaders({ 'Content-Type': 'application/json'});

    getQuestionCollection(checklist_id: number): Observable<Object>
    {
        return this.http.get(environment.API_ENDPOINT + `/api/questions/items/${checklist_id}`, { headers: this.headers })
    }

    newQuestionItem(value: any)
    {
        return this.http.put(environment.API_ENDPOINT + `/api/questions/item/new`, value, { headers: this.headers })
    }

    getQuestionById(question_id: number)
    {
        return this.http.get(environment.API_ENDPOINT + `/api/questions/item/${question_id}`, { headers: this.headers })
    }

    deleteQuestionById(question_id: number): Observable<Object>
    {
        return this.http.delete(environment.API_ENDPOINT + `/api/questions/item/delete/${question_id}`, { headers: this.headers })
    }

    updateQuestion(value: any, question_id: number)
    {
        return this.http.put(environment.API_ENDPOINT + `/api/questions/item/update/${question_id}`, value, { headers: this.headers })
    }

    storeSprintQuestions(maturity: number, questions: any[]): Observable<Object>
    {
        return this.http
            .put(environment.API_ENDPOINT + `/api/questions/store/${maturity}`, JSON.stringify({ questions }),
                { headers: this.headers })
    }
}