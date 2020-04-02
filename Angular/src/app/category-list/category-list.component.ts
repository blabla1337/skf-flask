import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CategoryService } from '../services/category.service';
import { Category } from '../models/category';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-category-list',
  templateUrl: './category-list.component.html',
  providers: [CategoryService]
})
export class CategoryComponent implements OnInit
{

  categoryForm: FormGroup;
  public delete: string;
  public categories: Category[];
  public isSubmitted: boolean;
  get formControls() { return this.categoryForm.controls; }

  constructor(private categoryService: CategoryService, private modalService: NgbModal, private formBuilder: FormBuilder) { }

  ngOnInit()
  {
    this.categoryForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
    })
    this.categoryList();
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
        err => 
        ('Getting the projects failed, contact an administrator! '));
  }

  storeCategory()
  {
    this.isSubmitted = true;
    if (this.categoryForm.invalid) {
      return;
    }
    this.categoryService.newCategory(this.categoryForm.value)
      .subscribe(
        () => this.categoryList(),
        () => console.log('error storing list')
      );
  }

  updateCategory(id: number)
  {
    this.isSubmitted = true;
    if (this.categoryForm.invalid) {
      return;
    }
    this.categoryService.updateCategory(id, this.categoryForm.value)
      .subscribe(
        () => this.categoryList(),
        () => console.log('error updating list')
      );
  }

  deleteCategory(id: number)
  {
    if (this.delete == 'DELETE') {
      this.categoryService.deleteCategory(id).subscribe(x =>
        this.categoryList())
    }
  }

  open(content)
  {
    this.modalService.open(content, { size: 'lg' }).result
  }

  updateContent(updateContent)
  {
    this.modalService.open(updateContent, { size: 'lg' }).result
  }

  getSet(name, description)
  {
    this.categories['name'] = name
    this.categories['description'] = description
    this.categoryForm.patchValue(this.categories)
  }

}
