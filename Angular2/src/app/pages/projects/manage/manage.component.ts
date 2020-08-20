import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';


import { ProjectService } from '../../../core/services/project.service';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class ProjectManageComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  public delete: string;
  public queryString;
  projectData: any;


  constructor(
    private modalService: NgbModal,
    private router: Router,
    private _projectService: ProjectService,
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Manage', active: true }];
    this.getProjects();
  }


  getProjects()
  {
    this._projectService.getProjectsCollection().subscribe(projects => this.projectData = projects)
  }

  deleteProject(id: number)
  {
    if (this.delete == 'DELETE') {
      this._projectService.deleteProject(id).subscribe(x => this.getProjects())
    }
  }

  projectModal(content: any)
  {
    this.modalService.open(content, { size: 'lg', centered: true });
  }

  onSubmit()
  {
    this.router.navigate(['/projects/manage']);
  }
}
