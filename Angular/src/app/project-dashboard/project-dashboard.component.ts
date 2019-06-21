import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { QuestionsService } from '../services/questions.service';
import { SprintService } from '../services/sprint.service'
import { Sprint } from '../models/sprint'
import { Questions } from '../models/questions'
import { ActivatedRoute } from '@angular/router';
import { NgForm } from '@angular/forms';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { ChecklistType } from '../models/checklist_type'
import { ChecklistService } from '../services/checklist.service'
import { Router } from '@angular/router'

@Component({
  selector: 'app-project-dashboard',
  templateUrl: './project-dashboard.component.html',
  providers: [QuestionsService, SprintService, ChecklistService]
})
export class ProjectDashboardComponent implements OnInit {

  closeResult: string;
  public preDevelopment: Questions[];
  public sprints: Questions[];
  public sprintResult: Sprint[];
  public questions: Questions[] = []
  public steps = false;
  public sprintName: string;
  public sprintDescription: string;
  public errors: string[] = [];
  public sprintID: number;
  public return: boolean;
  public delete: string;
  public idFromURL: number;
  public canDelete: boolean;
  public canEdit: boolean;
  public checklistTypeID: number;
  public checklistType: ChecklistType[] = [];
  public sprintStore: Sprint[] = [];

  constructor(
    private modalService: NgbModal,
    private questionsService: QuestionsService,
    private route: ActivatedRoute,
    private sprintService: SprintService,
    private checklistService: ChecklistService,
    private router: Router,
  ) { }

  ngOnInit() {
    this.checklistTypeList();
    this.getSprintStats();
    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canDelete = decodedJWT.privilege.includes('delete');
      this.canEdit = decodedJWT.privilege.includes('edit');
    }
  }

  selectQuestions() {
    this.questionsService.getQuestions(this.checklistTypeID).subscribe(
      questions => this.questions = questions,
      err => console.log('getting questions failed')
    )
  }


  // Temp storage for sprint questionaire
  storeSprint(form: NgForm) {
    localStorage.setItem('questions', JSON.stringify(form.value));
    return
  }

  newSprint() {
    this.errors = [];
    this.return = true;

    if (!this.sprintName) { this.errors.push('Sprint name was empty!'); this.return = false }
    if (!this.sprintDescription) { this.errors.push('Sprint description was empty!'); this.return = false; }
    if (this.return == false) { return; }
    this.sprintService.newSprint(this.sprintName, parseInt(this.idFromURL.toString(), 10), this.sprintDescription)
      .subscribe(res => { this.sprintID = res['sprintID'] }, error => console.log('error storing sprint'));
    this.steps = true;
  }

  newSprintQuestions() {

    const sprint_items = JSON.parse(localStorage.getItem('questions'));
    const count_sprint = Object.keys(sprint_items).length

    this.sprintStore = [];

    for (let i = 1; i < count_sprint + 1; i++) {
      if (sprint_items['answer' + i] == '0') {
        this.sprintStore.push({ 'projectID': Number(this.idFromURL), 'question_ID': Number(sprint_items['answer' + i]), 'result': 'False', 'sprintID': Number(this.sprintID), 'checklist_type': Number(this.checklistTypeID) });
      }
      if (sprint_items['sanswer' + i] == '') {
        this.sprintStore.push({ 'projectID': Number(this.idFromURL), 'question_ID': Number(sprint_items['answer' + i]), 'result': 'False', 'sprintID': Number(this.sprintID), 'checklist_type': Number(this.checklistTypeID)  });
      }
      if (sprint_items['answer' + i] != '0') {
        this.sprintStore.push({ 'projectID': Number(this.idFromURL), 'sprintID': Number(this.sprintID), 'question_ID': Number(sprint_items['answer' + i]), 'result': 'True', 'checklist_type': Number(this.checklistTypeID)  });
      }
    }

  setTimeout(() => {

    this.questionsService.newSprint(this.sprintStore, this.checklistTypeID).subscribe(() => { },
      err => console.log('Error Storing new questions for sprint'));
      this.getSprintStats();
  }, 1000);

this.steps = false;

  }

deleter(id: number) {
  if (this.delete == 'DELETE') {
    this.sprintService.delete(id).subscribe(x =>
      this.sprintService.getSprintStats(this.idFromURL).subscribe(
        resp => this.sprintResult = resp,
        err => console.log('Error getting sprint stats'))
    )
    return true;
  }
  return false;
}

getSprintStats() {
  this.route.params.subscribe(params => {
    this.idFromURL = params['id'];
    localStorage.setItem('tempParamID', params['id'])
    setTimeout(() => {
      this.sprintService.getSprintStats(this.idFromURL).subscribe(
        resp => this.sprintResult = resp,
        err => console.log('Error getting sprint stats'))
    }, 1000);
  });
}
open(content) {
  this.modalService.open(content, { size: 'lg' })
}

checklistTypeList() {
  this.checklistService
    .getChecklistTypeList()
    .subscribe(
      checklistType => {
        this.checklistType = checklistType;
      },
      err => console.log('errors went wrong!'));
}
}
