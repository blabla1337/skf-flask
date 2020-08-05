import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { ProjectService } from '../../../core/services/project.service';


@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class ProjectCreateComponent implements OnInit
{
  // bread crumb items
  breadCrumbItems: Array<{}>;
  public projectForm: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private _projectService: ProjectService
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Create', active: true }];

    this.projectForm = this.formBuilder.group({
      name: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      description: ['', [Validators.required]],
      version: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9.]+')]],
    });
    this.submit = false;
  }

  createProject()
  {
    this.submit = true;
    if (this.projectForm.invalid) {
      return;
    }
    this._projectService.createProject(this.projectForm.value).subscribe()
    this.router.navigate(['/projects/manage'])
  }

  /**
   * Returns form
   */
  get form() {
    return this.projectForm.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit() {
    this.submit = true;
  }

}
