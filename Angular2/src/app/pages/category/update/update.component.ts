import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

import { ChecklistCategoryService } from '../../../core/services/checklist_category.service'

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateCategoryComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  public validationform: FormGroup;
  public isSubmitted: boolean;
  private sub: any;
  public id: number;
  // Form Submission
  submit: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private route: ActivatedRoute,
    private _checklistCategoryService: ChecklistCategoryService) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Category' }, { label: 'Update', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this.validationform = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
    });

    this._checklistCategoryService
      .getChecklistCategoryById(this.id)
      .subscribe(item => this.validationform.patchValue(item))
    this.submit = false;
  }


  updateCategory()
  {
    this.submit = true;
    if (this.validationform.invalid) {
      return;
    }
    this._checklistCategoryService.updateChecklistCategory(this.id, this.validationform.value).subscribe()
    this.router.navigate(['/category/manage'])
  }

  get form()
  {
    return this.validationform.controls;
  }

  validSubmit()
  {
    this.submit = true;
  }


}
