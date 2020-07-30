import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class ChecklistCreateComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Form Validation
  validationform: FormGroup;

  // Form Submission
  submit: boolean;
  formsubmit: boolean;
  constructor(
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Create', active: true }];

     /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      title: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9 ]+')]],
      description: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9 ]+')]],
      status: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
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
