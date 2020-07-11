import { Component, OnInit } from '@angular/core';

import Swal from 'sweetalert2';

import { Labs } from './view.model';
import { labData } from './data';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class LabViewComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  labData: Labs[];

  constructor() { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Labs' }, { label: 'View', active: true }];
    this._fetchData();
  }

  /**
   * Checklists data fetches
   */
  private _fetchData() {
    this.labData = labData;
  }


  // Get Lab Address
  getLabAddress() {
    const labAPI = 'https://api6.ipify.org?format=json';
    Swal.queue([
      {
        title: 'Lab URL',
        text: 'This will bring you the url of the lab',
        confirmButtonText: 'Sounds Good',
        confirmButtonColor: '#8184B2',
        showLoaderOnConfirm: true,
        preConfirm: () => {
          return fetch(labAPI)
            .then(response => response.json())
            .then(data => Swal.insertQueueStep(data.ip))
            .catch(() => {
              Swal.insertQueueStep({
                title: 'Unable to get your lab address'
              });
            });
        }
      }
    ]);
  }

}
