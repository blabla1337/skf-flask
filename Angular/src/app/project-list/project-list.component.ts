import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ProjectService } from '../services/project.service';
import { Project } from '../models/project';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  providers: [ProjectService]
})
export class ProjectListComponent implements OnInit
{

  projectForm: FormGroup;
  public delete: string;
  public projects: Project[];
  public isSubmitted: boolean;
  public canManage: boolean;

  get formControls() { return this.projectForm.controls; }

  constructor(private _projectService: ProjectService, private modalService: NgbModal, private formBuilder: FormBuilder) { }

  ngOnInit()
  {

    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canManage = decodedJWT.privilege.includes('manage');
    }

    this.projectForm = this.formBuilder.group({
      name: ['', Validators.required],
      version: ['', Validators.required],
      description: ['', Validators.required],
    })

    this.projectList();
  }

  projectList()
  {
    this._projectService
      .getProjectList()
      .subscribe(
        projects =>
        {
          this.projects = projects;
        },
        err => console.log('Getting the projects failed, contact an administrator! '));
  }

  storeProject()
  {
    this.isSubmitted = true;
    if (this.projectForm.invalid) {
      return;
    }
    this._projectService.newProject(this.projectForm.value)
      .subscribe(
        () => this.projectList(),
        () => console.log('error storing list')
      );
  }

  deleteProject(id: number)
  {
    if (this.delete == 'DELETE') {
      this._projectService.deleteProject(id).subscribe(x =>
        this.projectList())
    }
  }

  open(content)
  {
    this.modalService.open(content, { size: 'lg' }).result
  }

}
