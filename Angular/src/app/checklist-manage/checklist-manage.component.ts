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
  public checklistID: string;
  public error: string;
  public delete: string;
  public canDelete: boolean;
  public idFromURL: number;
  public projects: any;

  constructor(private _checkListService: ChecklistService, private modalService: NgbModal, private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.idFromURL = params['id'];
      localStorage.setItem('checklist_type_id', params['id'])
    });

    // this.projectList();
    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes('delete');
    }
  }
  open(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }
}
