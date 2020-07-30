import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { Checklists } from '../../../core/models/checklists.model';
import { ChecklistService } from '../../../core/services/checklists.service';
import { checkData } from '../data';

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ChecklistsReadComponent implements OnInit {

  // Bread crumb item
  breadCrumbItems: Array<{}>;
  public queryString;
  public checklistDataCat: any;
  public checklistDataControls: any;

  checkData: Checklists[];

  // Collapse value
  public isCollapsed: boolean[] = [];

  constructor(
    private modalService: NgbModal,
    private _checklistCategoryService: ChecklistService
    ) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Read', active: true }];
    this._fetchData();
  }

   /**
   * Checklist data fetches
   */
  private _fetchData()
  {
    this._checklistCategoryService
      .getChecklistsCollection(Number(localStorage.getItem('categorySelector')))
      .subscribe(checklistCat => this.checklistDataCat = checklistCat);

      this._checklistCategoryService
      .getChecklistsControls(Number(1))
      .subscribe(checklistCon => this.checklistDataControls = checklistCon);
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) 
  {
    this.modalService.open(centerDataModal, { centered: true });
  }

  storeSprintLocalStorage(sprint_id: number)
  {
    //localStorage.setItem('questions', JSON.stringify(form.value));
    return
  }



}
