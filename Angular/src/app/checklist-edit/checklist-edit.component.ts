import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { QuestionPreService} from '../services/questions-pre.service'
import { QuestionsSprintService } from '../services/questions-sprint.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { Checklist } from '../models/checklist';
import { Knowledgebase } from '../models/knowledgebase';
import { Question_pre } from '../models/question_pre'
import { Question_sprint } from '../models/question_sprint'

@Component({
  selector: 'app-checklist-edit',
  templateUrl: './checklist-edit.component.html',
providers: [ChecklistService, QuestionPreService, QuestionsSprintService]
})
export class ChecklistEditComponent implements OnInit {

  constructor(
    private _checklistService: ChecklistService,
    private _questionsPreService: QuestionPreService,
    private _knowledgeService: KnowledgebaseService,
    private _questionsSprintService: QuestionsSprintService,
    private modalService: NgbModal,
    private router: Router,
  ) { }

  public idfromUrl: string;
  public error: string;
  public errors = [];
  public return: boolean;
  public delete:string;
  public succes: string;
  public canEdit: boolean;
  public knowledgebaseID: number;
  public checklist: Checklist[]
  public pre_dev: Question_pre[];
  public sprints: Question_sprint[];
  public kbID: string;
  public include_first: string;
  public include_always: string;
  public checklistID: number;
  public content: string;
  public question_sprint_ID: number;
  public question_pre_ID: number;
  public editChecklist:boolean;
  knowledgebaseItems: Knowledgebase[];

  ngOnInit() {
    this.idfromUrl = localStorage.getItem("tempParamID");
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes("edit");
    }
    this.getChecklistList();
    this.getKnowledgeItems();
    this.getPreQuestionList(Number(localStorage.getItem("tempParamID")));
    this.getSprintQuestionList(Number(localStorage.getItem("tempParamID")));
  }

  storeChecklistItem(){
    this.errors = [];  
    this.return = true;

    if (!this.idfromUrl) { this.errors.push("Checklist ID was not filled in"); this.return = false; }
    if (!this.checklistID) { this.errors.push("Checklist ID validation failed"); this.return = false; }
    if (!this.content) { this.errors.push("The checklist item name was not filled in"); this.return = false; }
    if (!this.kbID) { this.errors.push("There was no knowledgebase ID selected"); this.return = false; }
    if (!this.include_always) { this.errors.push("Include always choice was not made"); this.return = false; }
    if (!this.include_first) { this.errors.push("Include first choice was not made"); this.return = false; }
    
    if (this.return == false) { return; }
  
    this._checklistService.newChecklistItem(Number(this.idfromUrl), this.checklistID, this.content, Number(this.kbID), this.include_always, this.include_first, Number(this.question_sprint_ID), Number(this.question_pre_ID))
      .subscribe(
        () => this.getChecklistList(),
        () => this.errors.push("Error storing checklist item, potential duplicate checklist ID")
      );
  }

  updateChecklistItem(){

    this.errors = [];  
    this.return = true;

    if (!this.idfromUrl) { this.errors.push("Checklist ID was not filled in"); this.return = false; }
    if (!this.checklistID) { this.errors.push("Checklist ID validation failed"); this.return = false; }
    if (!this.content) { this.errors.push("The checklist item name was not filled in"); this.return = false; }
    if (!this.kbID) { this.errors.push("There was no knowledgebase ID selected"); this.return = false; }
    if (!this.include_always) { this.errors.push("Include always choice was not made"); this.return = false; }
    if (!this.include_first) { this.errors.push("Include first choice was not made"); this.return = false; }
    
    if (this.return == false) { return; }

    this.errors = [];
    this._checklistService.updateChecklistItem(Number(this.idfromUrl), this.checklistID, this.content, Number(this.kbID), this.include_always, this.include_first, Number(this.question_sprint_ID), Number(this.question_pre_ID))
      .subscribe(
        () => this.getChecklistList(),
        () => this.errors.push("Error updating checklist item, potential duplicate or incorrect checklist ID (1.2, 1.2, 2.1, etc)")
      );
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(requestData => this.knowledgebaseItems = requestData,
      err => this.error = "Error getting knowledge items, contact the administrator!"
    );
  }

  getChecklistList() {
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

  getPreQuestionList(checklistType:number){
    this._questionsPreService.getPreQuestions(checklistType).subscribe(
      pre_dev => this.pre_dev = pre_dev,
      err => console.log("getting pre dev questions failed")
    )
  }

  getSprintQuestionList(checklistType:number){
    this._questionsSprintService.getSprintQuestions(checklistType).subscribe(
      sprints => this.sprints = sprints,
      err => console.log("getting sprint questions failed")
    )  
  }

  back() {
    this.router.navigate(["/checklist-manage/", localStorage.getItem("tempParamID")]);
  }

  deleteChecklistItem(checklistID:string) {
    if (this.delete == "DELETE") {
      this._checklistService.deletechecklistItem(checklistID).subscribe(x =>
        //Get the new project list on delete 
        this.getChecklistList())
      this.delete = "";
    }
  }
  
  deleteChecklistItemModal(modalValue) {
    this.modalService.open(modalValue, { size: 'lg' })
  }

  newChecklistItemModal(modalValue) {
    this.modalService.open(modalValue, { size: 'lg' })
  }

  editItem(item:string[]){ 
    this.editChecklist = true 
    this.checklistID = item["checklist_items_checklistID"]
    this.content = item["checklist_items_content"]
    this.question_pre_ID = item["question_pre_ID"]
    this.question_sprint_ID = item["question_sprint_ID"]
    this.kbID = item["kb_item_id"]
    this.include_first = item["include_first"]
    this.include_always = item["include_always"]
  }
  readItem(){ 
    this.editChecklist = false
    this.checklistID = null
    this.content = null
    this.question_pre_ID = null
    this.question_sprint_ID = null
    this.kbID = null
    this.include_first = null
    this.include_always = null
  }
}
