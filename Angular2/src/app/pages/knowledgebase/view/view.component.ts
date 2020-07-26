import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

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
  public knowledgebaseForm: FormGroup;
  public categoryId: any;
  public queryString;

  get formControls() { return this.knowledgebaseForm.controls; }

  constructor(
    private modalService: NgbModal,
    private _knowledgebaseService: KnowledgebaseService,
    private _checklistCategoryService: ChecklistCategoryService
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'View', active: true }];
    this._fetchData();
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

  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }

  deleteKnowledgebaseItem(id: number)
  {
    this._knowledgebaseService.deleteknowledgebaseItem(id).subscribe(x => this._fetchData())
  }
}
