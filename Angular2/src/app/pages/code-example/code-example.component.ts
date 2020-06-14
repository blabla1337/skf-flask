import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-code-example',
  templateUrl: './code-example.component.html',
  styleUrls: ['./code-example.component.scss']
})
export class CodeExampleComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse declare
  isCollapsed: boolean;

  constructor() { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Code' }, { label: 'Examples', active: true }];

    // Collapse value
    this.isCollapsed = false;
  }

}
