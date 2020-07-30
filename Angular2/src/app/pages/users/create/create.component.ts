import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class UserCreateComponent implements OnInit 
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Form Validation
  public validationform: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor( 
    private formBuilder: FormBuilder
  ) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Create', active: true }];

    /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      firstName: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      lastName: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
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
