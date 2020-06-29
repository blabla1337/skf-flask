import { Component, OnInit } from '@angular/core';

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

}
