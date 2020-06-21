import { Component, OnInit } from '@angular/core';

import { Checklists } from '../checklists.model';
import { checkData } from '../data';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  checkData: Checklists[];

  constructor() { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'View', active: true }];

    this.checkData = checkData;
  }

}
