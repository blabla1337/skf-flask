import { Component, OnInit } from '@angular/core';

import { Codes } from './code-example.model';

import { codeData } from './data';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  codeData: Codes[];


  // Collapse declare
  isCollapsed: boolean;

  constructor() { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'View', active: true }];

    // Collapse value
    this.isCollapsed = true;

    this._fetchData();
  }

  /**
   * Code data fetches
   */
  private _fetchData() {
    this.codeData = codeData;
  }
}
