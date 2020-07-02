import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { knowledgeData } from '../data';
import { Knowledgebase } from '../knowledgebase.model';

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ReadComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];

  knowledgeData: Knowledgebase[];

  constructor(private modalService: NgbModal) { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'Read', active: true }];

    this._fetchData();
}

  /**
   * Knowledgebase data fetches
   */
  private _fetchData() {
    this.knowledgeData = knowledgeData;
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) {
    this.modalService.open(centerDataModal, { centered: true });
  }
}
