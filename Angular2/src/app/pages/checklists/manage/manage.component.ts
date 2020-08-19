import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { ChecklistCategoryService } from '../../../core/services/checklist_category.service'

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class CheckManageComponent implements OnInit
{

  checkData;

  public isCollapsed: boolean[] = [];

  // bread crumb items
  breadCrumbItems: Array<{}>;

  constructor(
    private modalService: NgbModal,
    private _checklistCategoryService: ChecklistCategoryService,
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Manage', active: true }];

  }

  getChecklistCategories()
  {
    this._checklistCategoryService
    .getChecklistCategoryCollection(Number(localStorage.getItem("categorySelector"))).subscribe()
  }

  centerModal(centerDataModal: any)
  {
    this.modalService.open(centerDataModal, { centered: true, size: 'lg' });
  }

}
