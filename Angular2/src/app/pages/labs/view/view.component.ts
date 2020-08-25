import { Component, OnInit } from '@angular/core';

import Swal from 'sweetalert2';

import { NgxSpinnerService } from 'ngx-spinner';
import { LabService } from '../../../core/services/lab.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class LabViewComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  public labData: any;
  public queryString;
  public queryLabel;
  public deployments;
  labLists: string[];
  lab: any;

  // tslint:disable-next-line: variable-name
  constructor(private _labService: LabService, private spinner: NgxSpinnerService, ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Labs' }, { label: 'View', active: true }];
    this._fetchData();
    this.labLists = ['SKF-Labs', 'Juice-Shop', 'Other Labs'];
  }

  /**
   * Labs data fetches
   */
  private _fetchData()
  {
    this._labService.getLabs().subscribe(lab => this.labData = lab);
  }


  // Get Lab Address
  // tslint:disable-next-line: variable-name
  getLabAddress(image_tag)
  {
    this.spinner.show()
    this._labService.deployLab(image_tag).subscribe(requestData =>
    {
      this.deployments = requestData
      this.spinner.hide();
      this.lab = this.deployments.split("\\");
      Swal.queue([
        {
          title: 'Lab URL',
          text: this.lab[3].substring(1),
          confirmButtonText: 'Close',
          confirmButtonColor: '#8184B2',
          showLoaderOnConfirm: true,
          preConfirm: () =>
          {
          }
        }
      ]);
    });
  }

  stopLabFromRunning(image_tag)
  {
    this.spinner.show()
    this._labService.deleteLab(image_tag).subscribe(requestData =>
    {
      this.deployments = requestData
      this.spinner.hide();
      Swal.queue([
        {
          title: 'Container message',
          text: this.deployments,
          confirmButtonText: 'Close',
          confirmButtonColor: '#8184B2',
          showLoaderOnConfirm: true,
          preConfirm: () =>
          {
          }
        }
      ]);
    })
  }
}
