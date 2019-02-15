import { Component, OnInit,ViewChild, ElementRef} from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { QuestionsSprintService } from '../services/questions-sprint.service';
import { ChecklistService } from '../services/checklist.service';
import { Checklist } from '../models/checklist';
import { Question_post } from '../models/question_post'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';


@Component({
  selector: 'app-questionnaire-sprint',
  templateUrl: './questionnaire-sprint.component.html',
  providers: [QuestionsSprintService, ChecklistService]
})
export class QuestionnaireSprintComponent implements OnInit {
  @ViewChild('sectionNeedToScroll') sectionNeedToScroll: ElementRef

  closeResult: string;
  public canDelete: boolean;
  public idfromUrl: string;
  public questionID: number;
  public questionName: string;
  public sprints: Question_post[] = [];
  public checklist: Checklist[];
  public correlatedChecklist: Checklist[];
  public error: string;
  public errors=[];
  public delete:string;
  public checklistID:number;
  public content:string;
  public kbID:number;
  public question_sprint_ID:number;
  public question_pre_ID:number;
  public include_first:string;
  public include_always:string;

  constructor(
    private modalService: NgbModal,
    private _questionsSprintService: QuestionsSprintService,
    private _checklistService:ChecklistService,
    private router: Router,
  ) { }

  ngOnInit() {
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
    }
    this.idfromUrl = localStorage.getItem("tempParamID");
    this.getQuestionList();
    this.getChecklistList();
  };

  getQuestionList(){
    this._questionsSprintService.getSprintQuestions(Number(localStorage.getItem("tempParamID"))).subscribe(
      sprints => this.sprints = sprints,
      err => console.log("getting pre dev questions failed")
    )
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

  getChecklistListItemsCorrelatedToSelectedQuestion() {
    this._questionsSprintService
      .getChecklistItemsOnPreQuestionID(Number(localStorage.getItem("questionID")))
      .subscribe(
        correlatedChecklist => {
        this.correlatedChecklist = correlatedChecklist;
        if (!this.checklist) {
          this.error = "There are no items correlated yey"
        }
      },
      err => this.error = "Getting the correlated controls failed, contact an administrator! ");
  }

  selectChecklistItems(){
    localStorage.setItem("questionID", this.questionID.toString())
    this.getChecklistListItemsCorrelatedToSelectedQuestion()
  }

  storeNewQuestion(){
    this.errors = [];    
    this._questionsSprintService.newQuestion(Number(localStorage.getItem("tempParamID")), this.questionName)
      .subscribe(
        () => this.getQuestionList(),
        () => this.errors.push("Error whilst adding user, potential duplicate email adres!")
      );
  }

  updateQuestion(){
    this.errors = [];    
    this._questionsSprintService.updateQuestion(Number(localStorage.getItem("tempParamID")), this.questionName, this.questionID)
      .subscribe(
        () => {this.getQuestionList()},
        () => this.errors.push("Error whilst adding user, potential duplicate email adres!")
      );
  }

  correlateQuestionToChecklistITem(checklistID:number, content:string, kbID:string, include_always:string, include_first:string, question_pre_ID:string){
    console.log(this.checklistID)
    this.errors = [];    
    this._checklistService.updateChecklistItem(Number(this.idfromUrl), checklistID, content, Number(kbID), include_always, include_first,  Number(localStorage.getItem("questionID")), Number(question_pre_ID))
      .subscribe(
        () => {this.getChecklistListItemsCorrelatedToSelectedQuestion(); this.getChecklistList()},
        () => this.errors.push("Adding the checklistID to the question did not happen!")
      );
  }

  removeQuestionFromChecklistITem(checklistID:number, content:string, kbID:string, include_always:string, include_first:string, question_pre_ID:string){
    console.log(this.checklistID)
    this.errors = [];    
    this._checklistService.updateChecklistItem(Number(this.idfromUrl), checklistID, content, Number(kbID), include_always, include_first, 0, Number(question_pre_ID))
      .subscribe(
        () => {this.getChecklistListItemsCorrelatedToSelectedQuestion(); this.getChecklistList()},
        () => this.errors.push("Adding the checklistID to the question did not happen!")
      );
  }

  deleteQuestion(){
    if (this.delete == "DELETE") {
      this._questionsSprintService.deleteQuestion(this.questionID).subscribe(x =>
        //Get the new project list on delete 
        this.getQuestionList())
      this.delete = "";
    }
    console.log(this.questionID)
  }

  addQuestionModal(add) {
    this.modalService.open(add, { size: 'lg' })
  }

  updateQuestionModal(update) {
    this.modalService.open(update, { size: 'lg' })
  }

  deleteQuestionModal(deletes) {
    this.modalService.open(deletes, { size: 'lg' })
  }

  back() {
    this.router.navigate(["/checklist-manage/", localStorage.getItem("tempParamID")]);
  }

  public gotoSection() {
    //this will provide smooth animation for the scroll
    this.sectionNeedToScroll.nativeElement.scrollIntoView({ behavior: 'smooth', block: 'center' })
}

}
