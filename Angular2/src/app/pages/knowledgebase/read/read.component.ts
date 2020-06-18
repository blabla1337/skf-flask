import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ReadComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse declare
  isCollapsed: boolean;

  constructor() { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'Read', active: true }];

    // Collapse value
    this.isCollapsed = false;

}
}
