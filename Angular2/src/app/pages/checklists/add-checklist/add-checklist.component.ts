import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-add-checklist',
  templateUrl: './add-checklist.component.html',
  styleUrls: ['./add-checklist.component.scss']
})
export class AddChecklistComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Form Validation
  validationform: FormGroup;
  typeValidationForm: FormGroup;

  // Form Submission
  submit: boolean;

  kbitem: string[];

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Create', active: true }];

    this.kbitem = ['knowledgebase-1', 'knowledgebase-2', 'knowledgebase-3', 'knowledgebase-4', 'knowledgebase-5', 'knowledgebase-6'];

    /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      checkid: ['', [Validators.required, Validators.pattern('[0-9]._-+')]],
      checktitle: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      maturitylvl: ['', [Validators.required, Validators.pattern('[0-9]._-+')]],
      cwe: ['', [Validators.required, Validators.pattern('[0-9]._-+')]],
    });
    this.submit = false;
  }

  /**
   * Returns form
   */
  get form()
  {
    return this.validationform.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit()
  {
    this.submit = true;
  }

}
