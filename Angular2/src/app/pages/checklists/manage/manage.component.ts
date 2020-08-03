import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { manageData } from './data';
import { Manage } from './manage.model';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class CheckManageComponent implements OnInit {

  checkTotal: Manage[];
  checkItems: Manage[];
  checkData;

  public isCollapsed: boolean[] = [];

  // bread crumb items
  breadCrumbItems: Array<{}>;

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Manage', active: true }];

    this._fetchData();
  }

  private _fetchData() {
    this.checkTotal = manageData.filter(t => t.status === 'Completed');
    this.checkItems = manageData.filter(t => t.status === 'Pending');
    this.checkData = manageData;
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) {
    this.modalService.open(centerDataModal, { centered: true, size: 'lg' });
  }

}
