import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

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

  public labData: any = [];
  public queryString;
  public queryLabel;
  public deployments;
  public labLists: string[];
  public lab: any = [];
  public status: any = [];

  // tslint:disable-next-line: variable-name
  constructor(
    private _labService: LabService, 
    private spinner: NgxSpinnerService, 
    private router: Router,
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Labs' }, { label: 'View', active: true }];
    this._fetchData();
    this.labLists = ['SKF-Labs', 'Juice-Shop', 'Other Labs'];
    this.showStatus();
  }

  /**
   * Labs data fetches
   */
  private _fetchData()
  {
    this.spinner.show();
    this._labService
    .getLabs()
    .subscribe(lab => {
      this.labData = lab;
      this.spinner.hide();
    });
  }

  showStatus()
  {
    this.status = JSON.parse(localStorage.getItem("Labs-deployed"));
    console.log(status)
  }

  // Get Lab Address
  // tslint:disable-next-line: variable-name
  getLabAddress(image_tag)
  {
    this.spinner.show()
    this._labService.deployLab(image_tag).subscribe(requestData =>
    {
      var lab_split;
      var labs_deployed = []
      this.deployments = requestData
      this.spinner.hide();
      if (this.deployments.split("\\")){
        lab_split = this.deployments.split("\\");
        this.lab = lab_split[3].substring(1);
        console.log(localStorage.getItem("Labs-deployed"));
        if (localStorage.getItem("Labs-deployed") === null){
          labs_deployed.push(image_tag);
          localStorage.setItem("Labs-deployed", JSON.stringify(labs_deployed));
        }else if(localStorage.getItem("Labs-deployed")){
          var stored = JSON.parse(localStorage.getItem("Labs-deployed"));
          stored.push(image_tag);
          localStorage.setItem("Labs-deployed", JSON.stringify(stored));
        }
      }else{
        this.lab = "Sorry somthing went wrong!";
      }
      Swal.queue([
        {
          title: 'Lab deployment URL',
          text: this.lab,
          confirmButtonText: 'Close',
          confirmButtonColor: '#8184B2',
          showLoaderOnConfirm: true,
          onClose: this.viewLabs,
          preConfirm: () =>
          {
          }
        }
      ]);
    });
  }

viewLabs(){
  this.router.navigate(['/labs/view'])
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
          title: 'Lab deployment Stopped',
          text: "The running lab has been stopped.",
          confirmButtonText: 'Close',
          confirmButtonColor: '#8184B2',
          showLoaderOnConfirm: true,
          onClose: this.viewLabs,
          preConfirm: () =>
          {
          }
        }
      ]);
    })
  }
}
