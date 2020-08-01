import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { ProjectService } from '../../../core/services/project.service';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class ProjectUpdateComponent implements OnInit
{
  breadCrumbItems: Array<{}>;
  id: number;
  private sub: any;
  public projectForm: FormGroup;
  public projectItem: any;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  get formControls() { return this.projectForm.controls; }

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private _projectService: ProjectService,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Project' }, { label: 'Update', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this.projectForm = this.formBuilder.group({
      name: ['', Validators.required],
      description: ['', Validators.required],
      version: ['', Validators.required],
    })

    this.projectItem = this._projectService
      .getProjectItem(this.id)
      .subscribe(item => this.projectForm.patchValue(item))

  }

  updateProjectItem()
  {
    this.submit = true;
    if (this.projectForm.invalid) {
      return;
    }
    this._projectService.updateProject(this.id, this.projectForm.value).subscribe()
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

