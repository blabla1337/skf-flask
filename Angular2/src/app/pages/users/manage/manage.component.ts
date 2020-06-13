import { Component, OnInit } from '@angular/core';

import { Users } from './manage.model';

import { usersData } from './data';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class ManageComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  usersData: Users[];

  // page
  currentpage: number;

  constructor() { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Details', active: true }];

    this.currentpage = 1;

    /**
     * Fetches the data
     */
    this._fetchData();
  }

  /**
   * Customers data fetches
   */
  private _fetchData() {
    this.usersData = usersData;
  }
}
