import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateCheckComponent implements OnInit {


  // bread crumb items
  breadCrumbItems: Array<{}>;
  public checklistForm: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor(private formBuilder: FormBuilder,
              private router: Router) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Item', active: true }];

    this.checklistForm = this.formBuilder.group({
      title: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      content: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
    });
    this.submit = false;
  }

  createChecklistItem()
  {
    this.submit = true;
    if (this.checklistForm.invalid) {
      return;
    }
  }

  /**
   * Returns form
   */
  get form() {
    return this.checklistForm.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit() {
    this.submit = true;
  }

}
