import { Component, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { QuestionPreService } from '../services/questions-pre.service';
import { QuestionsSprintService } from '../services/questions-sprint.service';
import { SprintService } from '../services/sprint.service'
import { Question_pre } from '../models/question_pre'
import { Sprint } from '../models/sprint'
import { Question_sprint } from '../models/question_sprint'
import { Router, ActivatedRoute, Params } from '@angular/router';
import { NgForm } from '@angular/forms';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';


@Component({
  selector: 'app-project-dashboard',
  templateUrl: './project-dashboard.component.html',
  providers: [QuestionPreService, QuestionsSprintService, SprintService]
})
export class ProjectDashboardComponent implements OnInit {

  closeResult: string;
  public preDevelopment: Question_pre[];
  public sprints: Question_sprint[];
  public sprintResult: Sprint[];
  public sprintStore: Question_sprint[] = []
  public steps: boolean = false;
  public sprintName: string;
  public sprintDescription: string;
  public errors: string[] = [];
  public sprintID: number;
  public return: boolean;
  public pre_dev_store: Question_pre[] = [];
  public delete: string;
  public idFromURL: number;
  public canDelete: boolean;
  public canEdit: boolean;
  constructor(
    private modalService: NgbModal,
    private questionPreService: QuestionPreService,
    private questionsSprintService: QuestionsSprintService,
    private route: ActivatedRoute,
    private sprintService: SprintService
  ) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
    this.idFromURL = params['id'];
    localStorage.setItem("tempParamID", params['id'])
    setTimeout(() => {
    this.sprintService.getSprintStats(this.idFromURL).subscribe(
    resp => this.sprintResult = resp,
    err => console.log("Error getting sprint stats"))
    }, 2500);
    });
    
    this.questionsSprintService
      .getSprintQuestions()
      .subscribe(
      (projectService) => { this.sprints = projectService },
      err => console.log("getting sprint questions failed"));

    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes("delete");
      this.canEdit = decodedJWT.privilege.includes("edit");
    }
  }

  newSprint() {
    this.errors = [];
    this.return = true;

    if (!this.sprintName) { this.errors.push("Sprint name was empty!"); this.return = false }
    if (!this.sprintDescription) { this.errors.push("Sprint description was empty!"); this.return = false; }
    if (this.return == false) { return; }
    this.sprintService.newSprint(this.sprintName, parseInt(this.idFromURL.toString(), 10), this.sprintDescription)
      .subscribe(res => { this.sprintID = res['sprintID'] }, error => console.log("error storing sprint"));
    this.steps = true;
  }

  newSprintQuestions(form?: NgForm) {
    this.sprintStore = [];
        for (let i = 1; i < 22 + 1; i++) {
          if (!form.value["sprint_answer" + i]) { form.value["sprint_answer" + i] = "False"; }
          this.sprintStore.push({ "projectID": parseInt(this.idFromURL.toString(), 10), "question_sprint_ID": i, "result": form.value["sprint_answer" + i], "sprintID": this.sprintID });
        }
    setTimeout(() => {
      this.questionsSprintService.newSprint(this.sprintStore).subscribe(() => { },
        err => console.log("Error Storing new questions for sprint"), () => {
            this.sprintService.getSprintStats(this.idFromURL).subscribe(
              resp => this.sprintResult = resp,
              err => console.log("Error getting sprint stats"))
        });
    }, 1000);

    this.steps = false;
  }

  deleter(id: number) {
    if (this.delete == "DELETE") {
      this.sprintService.delete(id).subscribe(x =>
          this.sprintService.getSprintStats(this.idFromURL).subscribe(
            resp => this.sprintResult = resp,
            err => console.log("Error getting sprint stats"))
      )
      return true;
    }
    return false;
  }


  open(content) {
    this.steps = false;
    this.delete = "";
    this.sprintDescription = ""
    this.sprintName = "";
    this.modalService.open(content, { size: 'lg' })
  }
}
