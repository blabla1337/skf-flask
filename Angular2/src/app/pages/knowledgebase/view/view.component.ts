import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { NgxSpinnerService  } from 'ngx-spinner';
import { Router } from '@angular/router';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service';
import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewKnowledebaseComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];
  public knowledgeData: any = [];
  public categoryData: any = [];
  public categoryId: any;
  public queryString;
  public delete: string;
  loading: boolean;

  constructor(
    private modalService: NgbModal,
    private router: Router,
    // tslint:disable-next-line: variable-name
    private _knowledgebaseService: KnowledgebaseService,
    // tslint:disable-next-line: variable-name
    private _checklistCategoryService: ChecklistCategoryService,
    private spinner: NgxSpinnerService,
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'View', active: true }];
    this._fetchData();

    // Load Spinner
    //this.spinner.show();
  }

  /**
   * Knowledgebase data fetches
   */
  private _fetchData()
  {
    this._knowledgebaseService
      .getKnowledgeBaseItemsCollection(Number(localStorage.getItem('categorySelector')))
      .subscribe(data => this.knowledgeData = data);

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);
  }

  /**
   * Open delete modal
   * @param deleteDataModal delete modal data
   */
  deleteModal(deleteDataModal: any)
  {
    this.modalService.open(deleteDataModal, { centered: true });
  }

  // tslint:disable-next-line: ban-types
  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }

  deleteKnowledgebaseItem(id: number)
  {
    this._knowledgebaseService.deleteknowledgebaseItem(id).subscribe(x => this._fetchData());
  }

  onSubmit()
  {
    this.router.navigate(['/knowledgebase/view']);
  }
}
