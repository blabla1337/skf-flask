import { Component, OnInit } from '@angular/core';

import { Checklists } from '../checklists.model';
import { checkData } from '../data';

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ChecklistsReadComponent implements OnInit {

  // Bread crumb item
  breadCrumbItems: Array<{}>;

  checkData: Checklists[];

  // Collapse value
  public isCollapsed: boolean[] = [];

  constructor() { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Read', active: true }];

    this._fetchData();
  }

  /**
   * Checklists data fetches
   */
  private _fetchData() {
    this.checkData = checkData;
  }

}
