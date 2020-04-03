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
import { Category } from '../models/category';
import { CategoryService } from '../services/category.service';

@Component({
  selector: 'app-project-dashboard',
  templateUrl: './project-dashboard.component.html',
  providers: [QuestionsService, SprintService, ChecklistService, CategoryService]
})
export class ProjectDashboardComponent implements OnInit
{

  closeResult: string;
  public preDevelopment: Questions[];
  public sprints: Questions[];
  public categories: Category[];
  public sprintResult: Sprint[];
  public questions: Questions[] = []
  public steps = false;
  public sprint_name: string;
  public sprint_descriptionription: string;
  public errors: string[] = [];
  public sprint_id: number;
  public return: boolean;
  public delete: string;
  public idFromURL: number;
  public canDelete: boolean;
  public canEdit: boolean;
  public checklist_type: number;
  public checklistType: ChecklistType[] = [];
  public sprintStore: Sprint[] = [];
  public selected: string;
  public oldSprints: string;
  public queryString: string;
  public maturity_id: number;
  public category_id: number;

  constructor(
    private modalService: NgbModal,
    private questionsService: QuestionsService,
    private route: ActivatedRoute,
    private sprintService: SprintService,
    private checklistService: ChecklistService,
    private categoryService: CategoryService
  ) { }

  ngOnInit()
  {
    this.route.params.subscribe(params =>
    {
      localStorage.setItem('project_id', params['id'])
    });
    this.getSprintStats();
    this.categoryList();
  }

  selectQuestions()
  {
    this.questionsService.getQuestions(this.checklist_type).subscribe(
      questions => this.questions = questions,
      err => console.log('getting questions failed')
    )
  }

  // Temp storage for sprint questionaire
  storeSprint(form: NgForm)
  {
    localStorage.setItem('questions', JSON.stringify(form.value));
    return
  }

  categoryList()
  {
    this.categoryService
      .getCategories()
      .subscribe(
        categories =>
        {
          this.categories = categories;
        },
        err => console.log('Getting the projects failed, contact an administrator! '));
  }

  newSprint()
  {
    this.errors = [];
    this.return = true;

    if (!this.sprint_name) { this.errors.push('Sprint name was empty!'); this.return = false }
    if (!this.sprint_descriptionription) { this.errors.push('Sprint description was empty!'); this.return = false; }
    if (this.return == false) { return; }

    this.sprintService.newSprint(this.sprint_name, Number(localStorage.getItem('project_id')), this.sprint_descriptionription)
      .subscribe(res => { this.sprint_id = res['sprint_id'] }, error => console.log('error storing sprint'));
    this.steps = true;
  }

  oldSprint()
  {
    this.sprint_id = this.oldSprints['sprint_id']
    this.sprint_name = this.oldSprints['sprint_name']
  }


  newSprintQuestions()
  {

    const sprint_items = JSON.parse(localStorage.getItem('questions'));
    const count_sprint = Object.keys(sprint_items).length

    this.sprintStore = [];

    for (let i = 1; i < count_sprint + 1; i++) {
      if (sprint_items['answer' + i] != '') {
        this.sprintStore.push({ 'project_id': Number(localStorage.getItem('project_id')), 'sprint_id': Number(this.sprint_id), 'question_id': Number(sprint_items['answer' + i]), 'result': 'True', 'checklist_type': Number(this.checklist_type), 'sprint_name': this.sprint_name });
      }
    }

    if (count_sprint == 0) {
      this.sprintStore.push({ 'project_id': Number(localStorage.getItem('project_id')), 'sprint_id': Number(this.sprint_id), 'question_id': 0, 'result': 'True', 'checklist_type': Number(this.checklist_type), 'sprint_name': this.sprint_name });
    }

  setTimeout(() => {
    this.questionsService.newSprint(this.checklist_type, this.maturity_id, this.sprintStore).subscribe(() => { },
      err => console.log('Error Storing new questions for sprint'));
      this.getSprintStats();
  }, 1000);

  this.steps = false;
  }

  deleter(sprint_id: number)
  {
    if (this.delete == 'DELETE') {
      this.sprintService.delete(sprint_id).subscribe(x =>
        this.sprintService.getSprintStats(Number(localStorage.getItem("project_id"))).subscribe(
          resp => this.sprintResult = resp,
          err => console.log('Error getting sprint stats'))
      )
      return true;
    }
    return false;
  }


  getSprintStats()
  {
    setTimeout(() =>
    {
      this.sprintService.getSprintStats(Number(localStorage.getItem("project_id"))).subscribe(
        resp => this.sprintResult = resp,
        err => console.log('Error getting sprint stats'))
    }, 1000);
  }

  getSprintStats()
  {
    setTimeout(() =>
    {
      this.sprintService.getSprintStats(Number(localStorage.getItem("project_id"))).subscribe(
        resp => this.sprintResult = resp,
        err => console.log('Error getting sprint stats'))
    }, 1000);
  }

  checklistTypeList(category_id: number)
  {
    this.checklistService
      .getChecklistTypeList(category_id)
      .subscribe(
        checklistType =>
        {
          this.checklistType = checklistType;
        },
        err => console.log('errors went wrong!'));
  }

  selectChecklistsOnChange()
  {
    this.checklistTypeList(this.category_id)
  }

  open(content)
  {
    this.selected = '';
    this.modalService.open(content, { size: 'lg' })
  }
}
