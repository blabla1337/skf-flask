import { Component, OnInit } from '@angular/core';
import { ChecklistService } from '../services/checklist.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-checklist-manage',
  templateUrl: './checklist-manage.component.html',
  providers: [ChecklistService]
})
export class ChecklistManageComponent implements OnInit {
  closeResult: string;
  public number: number;
  public checklistID : string;
  public error: string;
  public delete: string;
  public canDelete:boolean;
  public idFromURL: number;

  constructor(private _checkListService: ChecklistService, private modalService: NgbModal, private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.idFromURL = params['id'];
      localStorage.setItem("tempParamID", params['id'])
    });

    //this.projectList();
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
    }
  }

  /*
  deleter(id: number) {
    if (this.delete == "DELETE") {
      this._checkListService.delete(id).subscribe(x =>
        //Get the new project list on delete 
        this.projectList())
    }
  }

  projectList() {
    this._checkListService
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
*/
  open(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }
}
