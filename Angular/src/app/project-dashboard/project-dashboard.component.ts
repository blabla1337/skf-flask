import { Component, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { QuestionPreService } from '../services/questions-pre.service';
import { QuestionsSprintService } from '../services/questions-sprint.service';
import { SprintService } from '../services/sprint.service'
import { Question_pre } from '../models/question_pre'
import { Sprint } from '../models/sprint'
import { Question_sprint } from '../models/question_sprint'
import { Router, ActivatedRoute, Params } from '@angular/router';


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

  constructor(
    private modalService: NgbModal,
    private questions_pre: QuestionPreService,
    private questions_sprint: QuestionsSprintService,
    private route: ActivatedRoute,
    private sprintStatus : SprintService
  ) { }

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.sprintStatus.getSprintStats(params['id']).subscribe(
        resp => this.sprintResult = resp,
        err => console.log("Error getting sprint stats"))
    });

    this.questions_pre
      .getPreQuestions()
      .subscribe(
      projectService => this.preDevelopment = projectService,
      err => console.log("getting pre-development failed"));

    this.questions_sprint
      .getSprintQuestions()
      .subscribe(
      (projectService) => {this.sprints = projectService  },
      err => console.log("getting sprint questions failed"));
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
