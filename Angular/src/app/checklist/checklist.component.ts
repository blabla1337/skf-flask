import { Component } from '@angular/core';
import { ChecklistService } from '../services/checklist.service'
import { ChecklistType } from '../models/checklist_type';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Checklist } from '../models/checklist';
import { CategoryService } from '../services/category.service';
import { Category } from '../models/category';


@Component({
  selector: 'app-checklist',
  templateUrl: './checklist.component.html',
  providers: [ChecklistService, CategoryService],
})

export class ChecklistComponent
{
  public checklistTypes: ChecklistType[] = [];
  public checklistItems: Checklist[] = [];
  public categories: Category[] = [];
  public category_id: number;
  public queryString: string;
  public closeResult: string;
  public error: string;
  public checklist_type: number;
  public color: string;
  public selectUndefinedOptionValue: undefined = undefined;

  constructor(private checklistService: ChecklistService, private categoryService: CategoryService, private modalService: NgbModal) { }


  ngOnInit()
  {
    this.categoryList()
  }

  checklistTypeList(category_id: number)
  {
    this.checklistService
      .getChecklistTypeList(category_id)
      .subscribe(
        checklistTypes =>
        {
          this.checklistTypes = checklistTypes;
        },
        err => this.error = 'Getting the checklist types failed, contact an administrator! ');
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

  selectChecklistsFromCategory() {

    if (this.category_id === undefined || this.category_id === null) {
      return;
    }S

    this.checklistTypeList(this.category_id);
  }

  open(content, typeID: number)
  {
    this.checklistService
      .getChecklistByType(typeID)
      .subscribe(checklistItems => { this.checklistItems = checklistItems });
    this.modalService.open(content, { size: 'lg' })
  }
}
