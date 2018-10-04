import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { Checklist } from '../models/checklist';
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { Knowledgebase } from '../models/knowledgebase';

@Component({
  selector: 'app-checklist-edit',
  templateUrl: './checklist-edit.component.html',
  providers: [ChecklistService]
})
export class ChecklistEditComponent implements OnInit {

  constructor(
    private _checklistService: ChecklistService,
    private modalService: NgbModal,
    private router: Router,
    private _knowledgeService: KnowledgebaseService,
  ) { }

  public idfromUrl: string;
  public error: string;
  public errors = [];
  public succes: string;
  public canEdit: boolean;
  public knowledgebaseID: number;
  public checklist: Checklist[]
  public kbID: string;
  public include_first: boolean;
  public include_always: boolean;
  public checklistID: number;
  public content: string;
  public question_sprint_ID: number;
  public question_pre_ID: number;
  knowledgebaseItems: Knowledgebase[];

  ngOnInit() {
    this.idfromUrl = localStorage.getItem("tempParamID");
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes("edit");
    }
    this.checklistList();
    this.getKnowledgeItems();
  }

  checklistList() {
    this._checklistService
      .getChecklistByType(Number(localStorage.getItem("tempParamID")))
      .subscribe(
      checklist => {
        this.checklist = checklist;
        if (!this.checklist) {
          this.error = "There are no checklist types defined yet"
        }
      },
      err => this.error = "Getting the checklist types failed, contact an administrator! ");
  }

  storeChecklistItem(){
    this.errors = [];    
    this._checklistService.newChecklistItem(Number(this.idfromUrl), this.checklistID, this.content, Number(this.kbID), Boolean(this.include_always), Boolean(this.include_first), Number(this.question_sprint_ID), Number(this.question_pre_ID))
      .subscribe(
      err => this.errors.push("Error whilst adding user, potential duplicate email adres!")
      );
      this.checklistList();
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(requestData => this.knowledgebaseItems = requestData,
      err => this.error = "Error getting knowledge items, contact the administrator!"
    );
  }

  back() {
    this.router.navigate(["/checklist-manage/", localStorage.getItem("tempParamID")]);
  }

  open(modalValue) {
    this.modalService.open(modalValue, { size: 'lg' })
  }
}
