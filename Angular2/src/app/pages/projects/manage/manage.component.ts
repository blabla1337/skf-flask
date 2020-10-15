import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { NgxSpinnerService  } from 'ngx-spinner';
import { Router } from '@angular/router';
import { AppSettings } from '../../../global';

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
  public projectData: any = [];
  public loggedinUser: string;
  public loggedin = false;
  public priv: string;

  constructor(
    private modalService: NgbModal,
    private router: Router,
    private _projectService: ProjectService,
    private spinner: NgxSpinnerService,
  ) { }

  ngOnInit()
  {
    if(AppSettings.USER_PRIV != null){
      this.priv = AppSettings.USER_PRIV;
    }else{
      this.priv = "";
    }
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Manage', active: true }];
    this.getProjects();
  }


  getProjects()
  {
    this.spinner.show();
    this._projectService
    .getProjectsCollection()
    .subscribe(projects => {
      this.projectData = projects;
      this.spinner.hide();
      });
    }

  deleteProject(id: number)
  {
    if (this.delete == 'DELETE') {
      this._projectService.deleteProject(id).subscribe(x => this.getProjects())
    }
  }

  projectModal(content: any)
  {
    this.modalService.open(content, { centered: true, size: 'lg' });
  }

  onSubmit()
  {
    this.router.navigate(['/projects/manage']);
  }

  loggedIn()
  {
    this.loggedinUser = sessionStorage.getItem('Authorization');
    this.loggedin = true;
    return this.loggedinUser;
  }
}
