import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';

import { ChecklistCategoryService } from '../../../core/services/checklist_category.service'

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class CategoryManageComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  categoryData: any;
  public delete: string;

  constructor(
    private modalService: NgbModal,
    private router: Router,
    private _categoryService: ChecklistCategoryService) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Category' }, { label: 'Manage', active: true }];
    this.getCategoryCollection()
  }

  getCategoryCollection()
  {
    this._categoryService.getChecklistCategoryCollection().subscribe(category => this.categoryData = category)
  }

  deleteCategory(category_id: number)
  {
    if (this.delete == 'DELETE') {
      this._categoryService.deleteChecklistCategory(category_id).subscribe(x => this.getCategoryCollection());
    }
  }

  categoryModal(content: any)
  {
    this.modalService.open(content, { size: 'lg', centered: true });
  }

  onSubmit()
  {
    this.router.navigate(['/projects/manage']);
  }

}
