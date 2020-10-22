
import {map} from 'rxjs/operators';
import { Injectable } from '@angular/core';
import { Headers, Http } from '@angular/http';
import { Category } from '../models/category';
import { AppSettings } from '../globals';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import 'rxjs/Rx';

@Injectable()
export class CategoryService {

  constructor(private http: Http) { }
  public headers = new Headers({ 'Content-Type': 'application/json' });
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  getCategories(): Observable<Category[]> {
    return this.http.get(environment.API_ENDPOINT + '/checklist_category/items', { headers: this.headers }).pipe(
      map(response => response.json().items));
  }

  getSingleCategory(id: number): Observable<Category[]> {
    return this.http.get(environment.API_ENDPOINT + `/checklist_category/${id}`, { headers: this.headers }).pipe(
      map(response => response.json()));
  }

  newCategory(category:Category): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + '/checklist_category/new', JSON.stringify({
        name: category['name'],
        description: category['description']
      }),
      { headers: this.postHeaders }).pipe(
      map(a => { return a.json() }));
  }

  updateCategory(id: number , category: Category): Observable<any> {
    return this.http
      .put(environment.API_ENDPOINT + `/checklist_category/update/${id}`, JSON.stringify({
        name: category['name'],
        description: category['description']
      }),
      { headers: this.postHeaders }).pipe(
      map(a => { return a.json() }));
  }

  deleteCategory(id: number) {
    const url = environment.API_ENDPOINT + `/checklist_category/delete/${id}`;
    return this.http.delete(url, { headers: this.postHeaders }).pipe(
      map(
      data => data,
      error => console.log('failed to delete')))
  }




}
