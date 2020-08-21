import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateChecklistTypeComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  public checklistForm: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor(private formBuilder: FormBuilder,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Item', active: true }];

    this.checklistForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      visibility: [, Validators.required],
    });

    this.submit = false;
  }

  updateChecklistItem()
  {
    this.submit = true;
    if (this.checklistForm.invalid) {
      return;
    }
  }

  /**
   * Returns form
   */
  get form()
  {
    return this.checklistForm.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit()
  {
    this.submit = true;
  }

}
