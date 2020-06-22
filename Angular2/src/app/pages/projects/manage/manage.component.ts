import { Component, OnInit } from '@angular/core';

import { Project } from './manage.model';

import { projectData } from './data';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class ProjectManageComponent implements OnInit {

  // bread crumb items
 breadCrumbItems: Array<{}>;

 projectData: Project[];

 constructor() { }

 ngOnInit() {
   this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Manage', active: true }];

   this.projectData = projectData;
 }
}
