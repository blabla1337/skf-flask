import { Component, OnInit } from '@angular/core';
import { ChecklistService } from '../services/checklist.service';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { ChecklistType } from '../models/checklist_type';


@Component({
  selector: 'app-checklist-summary',
  templateUrl: './checklist-summary.component.html',
  providers: [ChecklistService]
})
export class ChecklistSummaryComponent implements OnInit {
  closeResult: string;
  checklistTypes: ChecklistType[];
  public number: number;
  public delete: string;
  public updateName: string;
  public updateDescription: string;
  public checklistType: string;
  public checklistDescription: string;
  public canDelete: boolean;
  public return: boolean;
  public errors: string[] = [];
  public error: string;
  public idFromURL: number;
  public queryString: string;

  constructor(
    private _checklistService: ChecklistService,
    private modalService: NgbModal,
  ) { }

  ngOnInit() {
    this.checklistTypeList()
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
    }
  }

  deleteChecklistType(id: number) {
    if (this.delete == "DELETE") {
      this._checklistService.deletechecklistType(id).subscribe(x =>
        //Get the new project list on delete 
        this.checklistTypeList())
      this.delete = "";
    }
  }

  updateChecklistType(id: number) {
    this.return = true;
    this.errors = [];
    console.log(this.checklistType)
    if (!this.checklistType) { this.errors.push("No checklistType was provided!"); this.return = false; }
    if (!this.checklistDescription) { this.errors.push("No description was provided!"); this.return = false; }
    if (this.return == false) { return; }
    this._checklistService.updateChecklistType(id, this.checklistType, this.checklistDescription).subscribe(x =>
      //Get the new project list on delete 
      this.checklistTypeList())
      this.checklistType = "";
      this.checklistDescription="";
  }

  storeChecklistType() {
    this.return = true;
    this.errors = [];
    if (!this.checklistType) { this.errors.push("No checklistType was provided!"); this.return = false; }
    if (!this.checklistDescription) { this.errors.push("No Description was provided!"); this.return = false; }
    if (this.return == false) { return; }

    this._checklistService.newChecklistTyoe(this.checklistType, this.checklistDescription)
      .subscribe(
        checklistTypes => this.checklistTypes = checklistTypes,
        err => this.errors.push("There was an error storing the new checklistType"),
        () => this.checklistTypeList()
      );

    this.checklistType = "";
    this.checklistDescription="";
  }

  checklistTypeList() {
    this._checklistService
      .getChecklistTypeList()
      .subscribe(
        checklistTypes => {
          this.checklistTypes = checklistTypes;
          if (!this.checklistTypes) {
            this.error = "There are no checklist types defined yet"
          }
        },
        err => this.error = "Getting the checklist types failed, contact an administrator! ");
  }

  open(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  deleteContent(deleteContent) {
    this.modalService.open(deleteContent, { size: 'lg' }).result
  }

  updateContent(updateContent, foo) {
    this.checklistType = foo;
    this.modalService.open(updateContent, { size: 'lg' }).result
  }

  getSet(checklistType, checklistDescription){
    this.checklistType = checklistType;
    this.checklistDescription = checklistDescription;
  }
} 
