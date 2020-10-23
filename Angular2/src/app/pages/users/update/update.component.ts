import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UserUpdateComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Form Validation
  validationform: FormGroup;

  // Form Submission
  submit: boolean;
  formsubmit: boolean;

  constructor( private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Create', active: true }];

    /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.pattern('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$')]],
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
