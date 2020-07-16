import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';

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

  // Collapse value
  public isCollapsed: boolean[] = [];

  constructor(private modalService: NgbModal,
              private router: Router) { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'View', active: true }];

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
    this.modalService.open(centerDataModal, { size: 'lg', centered: true });
  }

  updateCode() {
    this.router.navigate(['./code-example/edit']);
  }

  deleteCode() {}
}
