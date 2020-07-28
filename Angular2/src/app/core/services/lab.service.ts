
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
    providedIn: 'root'
})

export class LabService
{

    constructor(
        private http: HttpClient,
    ) { }

    public authHeader = new HttpHeaders({ 'Content-Type': 'application/json', 'Authorization': sessionStorage.getItem("Authorization") });

    getLabs()
    {
        return this.http.get(environment.API_ENDPOINT + '/api/interactive_labs/items')
    }

    deployLab(image_tag)
    {
      return this.http.get(environment.API_ENDPOINT + `/interactive_labs/deployments/${image_tag}`, { headers: this.authHeader })
    }
  
    deleteLab(image_tag)
    {
      return this.http.get(environment.API_ENDPOINT + `/interactive_labs/delete-deployments/${image_tag}`, { headers: this.authHeader })
    }
}