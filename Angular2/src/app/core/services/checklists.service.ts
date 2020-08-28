
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})

export class ChecklistService
{

  constructor(
    private http: HttpClient,
  ) { }

  public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

  /**
 * types
 **/

  getChecklistsCollection(category_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist_types/types/${category_id}`, { headers: this.authHeader })
  }

  getChecklistById(checklist_type_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist_types/type/${checklist_type_id}`, { headers: this.authHeader })
  }

  createChecklistType(value: any, category_id: number)
  {
    return this.http.put(environment.API_ENDPOINT + `/api/checklist_types/create/${category_id}`, value, { headers: this.authHeader })
  }

  updateChecklistType(value: any, checklist_type_id: number)
  {
    return this.http.put(environment.API_ENDPOINT + `/api/checklist_types/update/${checklist_type_id}`, value, { headers: this.authHeader })
  }

  deleteChecklistType(checklist_type_id: number)
  {
    return this.http.delete(environment.API_ENDPOINT + `/api/checklist_types/delete/${checklist_type_id}`, { headers: this.authHeader })
  }


  /**
   * items
   **/

  getChecklistItems(checklist_type_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist/items/${checklist_type_id}`, { headers: this.authHeader })
  }

  getChecklistItemById(checklist_type_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist/item/${checklist_type_id}`, { headers: this.authHeader })
  }

  deleteChecklistItemById(requirement_id: number)
  {
    return this.http.delete(environment.API_ENDPOINT + `/api/checklist/delete/item/${requirement_id}`, { headers: this.authHeader })
  }

  createChecklistItem(value: any, checklist_type_id: number)
  {
    return this.http.put(environment.API_ENDPOINT + `/api/checklist/new/item/type/${checklist_type_id}`, value, { headers: this.authHeader })
  }

  updateChecklistItem(value: any, checklist_id: number)
  {
    return this.http.put(environment.API_ENDPOINT + `/api/checklist/update/item/${checklist_id}`, value, { headers: this.authHeader })
  }

  getChecklistItemsCorrelatedToQuestion(question_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist/item/question_sprint/${question_id}`, { headers: this.authHeader })
  }

  updateChecklisteItemCorrelationToQuestion(item_id: number, question_id: number)
  {
    return this.http.get(environment.API_ENDPOINT + `/api/checklist/update/item/correlation/${item_id}/question/${question_id}`, { headers: this.authHeader })
  }

}
