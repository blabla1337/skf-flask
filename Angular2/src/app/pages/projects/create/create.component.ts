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
  public isSubmitted: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private _projectService: ProjectService) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Create', active: true }];

    this.projectForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      version: ['', Validators.required],
    })

  }

  createProject()
  {
    this.isSubmitted = true;
    if (this.projectForm.invalid) {
      return;
    }
    this._projectService.createProject(this.projectForm.value).subscribe()
    this.router.navigate(['/projects/manage'])
  }
}
