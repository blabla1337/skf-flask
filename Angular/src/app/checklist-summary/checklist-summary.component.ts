import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ChecklistService } from '../services/checklist.service';
import { CategoryService } from '../services/category.service';

import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ChecklistType } from '../models/checklist_type';
import { Category } from '../models/category';

@Component({
  selector: 'app-checklist-summary',
  templateUrl: './checklist-summary.component.html',
  providers: [ChecklistService, CategoryService]
})

export class ChecklistSummaryComponent implements OnInit
{
  public checklistForm: FormGroup;
  public checklistTypes: ChecklistType[];
  public categories: Category[];
  public delete: string;
  public idFromURL: number;
  public queryString: string;
  public isSubmitted: boolean;
  public category_id: number;
  public selectUndefinedOptionValue: undefined = undefined;

  get formControls() { return this.checklistForm.controls; }

  constructor(private _checklistService: ChecklistService, private categoryService: CategoryService, private modalService: NgbModal, private formBuilder: FormBuilder) { }

  ngOnInit()
  {
    this.checklistForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      visibility: ['', Validators.required],
    })
    this.categoryList();
  }

  newChecklistType()
  {
    this.isSubmitted = true;
    if (this.checklistForm.invalid) {
      return;
    }
    this._checklistService.newChecklistType(this.category_id, this.checklistForm.value)
      .subscribe(
        () => this.checklistTypeList(this.category_id),
        () => console.log('There was an error storing the new checklistType')
      );
  }

  updateChecklistType(id: number)
  {
    this.isSubmitted = true;
    if (this.checklistForm.invalid) {
      return;
    }

    if (this.checklistForm.value['visibility'] == "True") {
      this.checklistForm.value['visibility'] = 1
    } else {
      this.checklistForm.value['visibility'] = 0
    }

    this._checklistService.updateChecklistType(id, this.checklistForm.value).subscribe(x =>
      // Get the new project list on delete
      this.checklistTypeList(this.category_id))
  }

  checklistTypeList(category_id: number)
  {
    this._checklistService
      .getChecklistTypeList(category_id)
      .subscribe(
        checklistTypes =>
        {
          this.checklistTypes = checklistTypes;
        },
        () => console.log('Getting the checklist types failed, contact an administrator! '))
  }

  categoryList()
  {
    this.categoryService
      .getCategories()
      .subscribe(
        categories =>
        {
          this.categories = categories;
        },
        err => console.log('Getting the projects failed, contact an administrator! '));
  }

  deleteChecklistType(id: number)
  {
    if (this.delete == 'DELETE') {
      this._checklistService.deleteChecklistType(id).subscribe(x =>
        // Get the new project list on delete
        this.checklistTypeList(this.category_id))
      this.delete = '';
    }
  }

  selectChecklistsFromCategory()
  {
    this.checklistTypeList(this.category_id);
    localStorage.setItem("category_id", this.category_id.toString());
  }

  open(content)
  {
    this.modalService.open(content, { size: 'lg' }).result
  }

  deleteContent(deleteContent)
  {
    this.modalService.open(deleteContent, { size: 'lg' }).result
  }

  updateContent(updateContent)
  {
    this.modalService.open(updateContent, { size: 'lg' }).result
  }

  getSet(name, description, visibility)
  {
    this.checklistTypes['name'] = name
    this.checklistTypes['description'] = description
    this.checklistTypes['visibility'] = visibility
    this.checklistForm.patchValue(this.checklistTypes)
  }
}