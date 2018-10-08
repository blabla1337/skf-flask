import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { QuestionPreService } from '../services/questions-pre.service';
import { ChecklistService } from '../services/checklist.service';
import { Checklist } from '../models/checklist';
import { Question_pre } from '../models/question_pre'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';


@Component({
  selector: 'app-questionnaire-pre',
  templateUrl: './questionnaire-pre.component.html',
  providers: [QuestionPreService, ChecklistService]
})
export class QuestionnairePreComponent implements OnInit {

  closeResult: string;
  public canDelete: boolean;
  public idfromUrl: string;
  public questionID: number;
  public questionName: string;
  public pre_dev: Question_pre[];
  public checklist: Checklist[]
  public error: string;
  public errors=[];
  public delete:string;

  constructor(
    private modalService: NgbModal,
    private _questionsPreService: QuestionPreService,
    private _checklistService:ChecklistService,
    private router: Router,
  ) { }

  ngOnInit() {
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
    }
    this.idfromUrl = localStorage.getItem("tempParamID");
    this.getPreQuestionList();
    this.getChecklistList();
  };

  getPreQuestionList(){
    this._questionsPreService.getPreQuestions(Number(localStorage.getItem("tempParamID"))).subscribe(
      pre_dev => this.pre_dev = pre_dev,
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

  selectChecklistItems(){
    console.log(this.questionID)
  }

  storeNewQuestion(){
    this.errors = [];    
    this._questionsPreService.newQuestion(localStorage.getItem("tempParamID"), this.questionName)
      .subscribe(
        () => this.getPreQuestionList(),
        () => this.errors.push("Error whilst adding user, potential duplicate email adres!")
      );
  }

  updateQuestion(){
    this.errors = [];    
    this._questionsPreService.updateQuestion(localStorage.getItem("tempParamID"), this.questionName, this.questionID)
      .subscribe(
        () => this.getPreQuestionList(),
        () => this.errors.push("Error whilst adding user, potential duplicate email adres!")
      );
  }

  deleteQuestion(){
    if (this.delete == "DELETE") {
      this._questionsPreService.deleteQuestion(this.questionID).subscribe(x =>
        //Get the new project list on delete 
        this.getPreQuestionList())
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

}
