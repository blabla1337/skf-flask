import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { Projects } from './view.model';
import { projectData } from './data';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ProjectViewComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  projectData: Projects[];

  constructor(private modalService: NgbModal) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'View', active: true }];

    this.projectData = projectData;
  }

  /**
   * Open modal
   * @param content modal content
   */
  verificationModal(content: any) {
    this.modalService.open(content, { size: 'lg' });
  }

}
