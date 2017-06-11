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


@Component({
  selector: 'app-project-dashboard',
  templateUrl: './project-dashboard.component.html',
  providers: [QuestionPreService, QuestionsSprintService, SprintService]
})
export class ProjectDashboardComponent implements OnInit {

  closeResult: string;
  public preDevelopment: Question_pre[];
  public sprints: Question_sprint[];
  private sprintResult: Sprint[];
  private sprintStore: Question_sprint[] = []
  public steps: boolean = false;
  public sprintName: string;
  public sprintDescription: string;
  public errors: string[] = [];
  public sprintID: number;
  public return: boolean;
  public pre_dev_store: Question_pre[] = [];

  constructor(
    private modalService: NgbModal,
    private questionPreService: QuestionPreService,
    private questionsSprintService: QuestionsSprintService,
    private route: ActivatedRoute,
    private sprintService: SprintService
  ) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.sprintService.getSprintStats(params['id']).subscribe(
        resp => this.sprintResult = resp,
        err => console.log("Error getting sprint stats"))
    });

    this.questionPreService
      .getPreQuestions()
      .subscribe(
      projectService => this.preDevelopment = projectService,
      err => console.log("getting pre-development failed"));

    this.questionsSprintService
      .getSprintQuestions()
      .subscribe(
      (projectService) => { this.sprints = projectService },
      err => console.log("getting sprint questions failed"));
  }

  newSprint() {
    this.errors = [];
    this.return = true;

    if (!this.sprintName) { this.errors.push("Sprint name was empty!"); this.return = false }
    if (!this.sprintDescription) { this.errors.push("Sprint description was empty!"); this.return = false; }
    if (this.return == false) { return; }

    this.steps = true;

  }

  newSprintQuestions(form: NgForm) {
    this.sprintStore = [];
    this.route.params.subscribe(params => {
      this.sprintService.newSprint(this.sprintName, parseInt(params['id'], 10), this.sprintDescription)
        .subscribe(res => { this.sprintID = res['sprintID'] }, error => console.log("error storing sprint"), () => {

          let count_sprint = Object.keys(form.value).length

          this.route.params.subscribe(params => {
            for (let i = 1; i < count_sprint + 1; i++) {
              if (form.value["sprint_answer" + i].toString() == "") { form.value["sprint_answer" + i] = "False"; }
              this.sprintStore.push({ "projectID": parseInt(params['id'], 10), "question_sprint_ID": i, "result": form.value["sprint_answer" + i].toString(), "sprintID": this.sprintID });
            }
          });
        });
    });

    setTimeout(() => {
      this.questionsSprintService.newSprint(this.sprintStore).subscribe(() => { },
        err => console.log("Error Storing new questions for sprint"));
    }, 1000);
  }

  updatePre(form: NgForm) {
    let count_pre = Object.keys(form.value).length


    for (let i = 1; i < count_pre + 1; i++) {
      if (form.value["pre_dev_answer" + i].toString() == "") { form.value["pre_dev_answer" + i] = "False"; }
      this.pre_dev_store.push({ "question_pre_ID": i, "result": form.value["pre_dev_answer" + i].toString() });
    }

    this.route.params.subscribe(params => {
      this.questionPreService.updatePre(params['id'], this.pre_dev_store).subscribe(() => { },
        err => console.log("Error Storing new questions for sprint"));
    });

  }

  open(content) {
    this.modalService.open(content, { size: 'lg' }).result.then((result) => {
      this.closeResult = 'Closed with: ${result}';
    }, (reason) => {
      this.closeResult = 'Dismissed ${this.getDismissReason(reason)}';
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }

}
