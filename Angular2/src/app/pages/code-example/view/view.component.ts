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
export class CodeViewComponent implements OnInit 
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];
  public codeData: any = [];
  public categoryData: any = [];
  public codeExamples: FormGroup;

  get formControls() { return this.codeExamples.controls; }

  constructor(
    private modalService: NgbModal,
    private _knowledgebaseService: CodeExamplesService,
    private _checklistCategoryService: ChecklistCategoryService
  ) { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'View', active: true }];

    this._fetchData();
  }

  /**
   * Knowledgebase data fetches
   */
  private _fetchData()
  {
    this._knowledgebaseService
      .getCode(Number(localStorage.getItem('categorySelector')))
      .subscribe(data => this.codeData = data);

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any)
  {
    this.modalService.open(centerDataModal, { size: 'lg', centered: true });
  }

  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }

  deleteKnowledgebaseItem(id: number)
  {
    this._knowledgebaseService.deleteCodeExample(id).subscribe(x => this._fetchData())
  }
}
