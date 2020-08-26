import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { NgxSpinnerService  } from 'ngx-spinner';

import { ChecklistService } from '../../../core/services/checklists.service';
import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  
  public queryString;
  public checklistData: any = [];
  public delete: string;
  public catSelector: number;
  public categoryData: any = [];

  constructor(
    private modalService: NgbModal,
    // tslint:disable-next-line: variable-name
    private _checklistService: ChecklistService,
    // tslint:disable-next-line: variable-name
    private _checklistCategoryService: ChecklistCategoryService,
    private spinner: NgxSpinnerService,
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'View', active: true }];
    this.catSelector = Number(localStorage.getItem('categorySelector'));
    this._fetchData();
  }

  /**
   * Checklist data fetches
   */
  private _fetchData()
  {
    this.spinner.show();
    this._checklistService
      .getChecklistsCollection(Number(localStorage.getItem('categorySelector')))
      .subscribe(checklist => {
        this.checklistData = checklist;
        this.spinner.hide();
      });

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);
  }

  // tslint:disable-next-line: ban-types
  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }

  deleteChecklistType(id: number)
  {
    if (this.delete === 'DELETE') {
      this._checklistService.deleteChecklistType(id).subscribe(x => this._fetchData());
    }
  }

  showModal(content: any)
  {
    this.modalService.open(content, { size: 'sm', centered: true });
  }

}
