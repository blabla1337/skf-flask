import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { Checklists } from '../../../core/models/checklists.model';
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

  constructor(private modalService: NgbModal) { }

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

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) {
    this.modalService.open(centerDataModal, { centered: true });
  }

}
