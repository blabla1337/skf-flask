import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { CodeExamplesService } from '../../../core/services/code-examples.service';
import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ViewCodeComponent implements OnInit 
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];
  public codeData: any = [];
  public categoryData: any = [];
  public codeExampleForm: FormGroup;
  public queryString;

  get formControls() { return this.codeExampleForm.controls; }

  constructor(
    private modalService: NgbModal,
    private _codeExamplesService: CodeExamplesService,
    private _checklistCategoryService: ChecklistCategoryService
  ) { }

  ngOnInit() 
  {
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'View', active: true }];
    this._fetchData();
  }

  /**
   * Knowledgebase data fetches
   */
  private _fetchData()
  {
    this._codeExamplesService
      .getCode(Number(localStorage.getItem('categorySelector')))
      .subscribe(data => this.codeData = data);

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);
  }

  /**
   * Open delete modal
   * @param deleteDataModal center modal data
   */
  deleteModal(deleteDataModal: any) 
  {
    this.modalService.open(deleteDataModal, { size: 'sm', centered: true });
  }

  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }

  deleteCodeExample(code_id: number)
  {
    this._codeExamplesService.deleteCodeExample(code_id).subscribe(x => this._fetchData())
  }
}
