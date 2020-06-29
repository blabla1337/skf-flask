import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

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

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'View', active: true }];
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
