import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service';
import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';

@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ReadComponent implements OnInit
{


  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean[] = [];
  public knowledgeData: any = [];
  public categoryData: any = [];
  public knowledgebaseForm: FormGroup;

  get formControls() { return this.knowledgebaseForm.controls; }

  constructor(
    private modalService: NgbModal,
    private _knowledgebaseService: KnowledgebaseService,
    private _checklistCategoryService: ChecklistCategoryService,
    private formBuilder: FormBuilder
  ) { }

  ngOnInit()
  {
    //move the category selector to a place where it sets a default value
    localStorage.setItem('categorySelector', '1')

    /** 
    this.knowledgebaseForm = this.formBuilder.group({
      firstname: ['', Validators.required],
      surname: ['', Validators.required],
      email: ['', [Validators.required, Validators.minLength(4)]],
    })
    */

   this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'Read', active: true }];
   this._fetchData();    this._fetchData();
  }

  /**
   * Knowledgebase data fetches
   */
  private _fetchData()
  {
    this._knowledgebaseService
      .getKnowledgeBaseItems(Number(localStorage.getItem('categorySelector')))
      .subscribe(data => this.knowledgeData = data);

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
    this.modalService.open(centerDataModal, { centered: true });
  }

  setCategorySelectorId(categoryId: Number)
  {
    localStorage.setItem('categorySelector', categoryId.toString());
    this._fetchData();
  }
}
