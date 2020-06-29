import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { Codes } from './code-example.model';

import { codeData } from './data';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class CodeViewComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  codeData: Codes[];

  // Collapse declare
  isCollapsed: boolean;

  constructor(private modalService: NgbModal) { }

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

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) {
    this.modalService.open(centerDataModal, { centered: true });
  }

}
