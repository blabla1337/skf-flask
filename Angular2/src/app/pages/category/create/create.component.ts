import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateCategoryComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;
  public validationform: FormGroup;
  public isSubmitted: boolean;

  // Form Submission
  submit: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Category' }, { label: 'Create', active: true }];

    /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      title: ['', [Validators.required, Validators.pattern('[0-9]._-+')]],
      content: ['', Validators.required],
    });
    this.submit = false;
  }

  /**
   * Returns form
   */
  get form() {
    return this.validationform.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit() {
    this.submit = true;
  }

}
