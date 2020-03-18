import { Component, OnInit } from '@angular/core';
import { HeaderComponent } from '../header/header.component';
import { LabService } from '../services/lab.service'
import { Labs } from '../models/labs'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

@Component({
  selector: 'app-dashboard',
  templateUrl: './labs.component.html',
  providers: [LabService]
})

export class LabsComponent implements OnInit
{

  public canEdit: boolean;
  public labs: Labs[] = [];
  public error: string;
  public queryString: string;
  public deployments = "Your deployment information will be displayed here! (please be patient, loading might take a while)"

  constructor(public _labService: LabService) { }

  ngOnInit()
  {
    this.getLabItems();

    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes('edit');
    }
  }

  getLabItems()
  {
    this._labService.getLabs().subscribe(requestData => this.labs = requestData,
      err => this.error = 'Error getting labs, contact the administrator!'
    );
  }

  deployContainer(image_tag) 
  {
    this._labService.deployLab(image_tag).subscribe(requestData => this.deployments = requestData,
      err => this.error = 'Error getting labs, contact the administrator!'
    );
  }

  deleteContainer(image_tag)
  {
    this._labService.deleteLab(image_tag).subscribe(requestData => this.deployments = requestData,
      err => this.error = 'Error getting labs, contact the administrator!'
    );
  }

}
