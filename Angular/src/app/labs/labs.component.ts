import { Component, OnInit } from '@angular/core';
import {HeaderComponent} from '../header/header.component';
import { LabService } from '../services/lab.service'
import {Labs} from '../models/labs'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

@Component({
  selector: 'app-dashboard',
  templateUrl: './labs.component.html',
  providers: [LabService]
})

export class LabsComponent implements OnInit {

  public canEdit: boolean;
  public labs: Labs[] = [];
  public error: string;
  public queryString: string;
  
  constructor(public _labService: LabService) { }

  ngOnInit() {
    this.getLabItems();

    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes("edit");
    }
  }

  getLabItems() {
    this._labService.getLabs().subscribe(requestData => this.labs = requestData,
      err => this.error = "Error getting labs, contact the administrator!"
    );
  }

}
