import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../services/project.service';
import { Project } from '../models/project';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Observable } from 'rxjs/Rx';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

@Component({
  selector: 'app-project-list',
  templateUrl: './project-list.component.html',
  providers: [ProjectService]
})
export class ProjectListComponent implements OnInit {
  projects: Project[];
  closeResult: string;
  public number: number;
  public error: string;
  public delete: string;
  public canDelete:boolean;

  constructor(private _projectService: ProjectService, private modalService: NgbModal) { }

  ngOnInit() {
    this.projectList();
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
    }
  }

  deleter(id: number) {
    if (this.delete == "DELETE") {
      this._projectService.delete(id).subscribe(x =>
        //Get the new project list on delete 
        this.projectList())
    }
  }

  projectList() {
    this._projectService
      .getProjects()
      .subscribe(
      projects => {
        this.projects = projects;
        if (!this.projects) {
          this.error = "There are no projects to show!"
        }
      },
      err => this.error = "Getting the projects failed, contact an administrator! ");
  }

  open(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }
}
