import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ChecklistService } from '../../../../core/services/checklists.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateChecklistTypeComponent implements OnInit
{


  // bread crumb items
  breadCrumbItems: Array<{}>;
  public checklistForm: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor(
    private _checklistService: ChecklistService,
    private formBuilder: FormBuilder,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Types create', active: true }];

    this.checklistForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      visibility: [, Validators.required],
    });
    this.submit = false;
  }

  createChecklistType()
  {
    this.submit = true;
    if (this.checklistForm.invalid) {
      return;
    }

    if (this.checklistForm.value['visibility'] == "True") {
      this.checklistForm.value['visibility'] = 1
    } else {
      this.checklistForm.value['visibility'] = 0
    }

    this._checklistService.createChecklistType(this.checklistForm.value, Number(localStorage.getItem("categorySelector"))).subscribe(
      () => this.router.navigate(["/checklists/view"])
    )
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
