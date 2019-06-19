import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../services/project.service'
import { QuestionsService } from '../services/questions.service'
import { SprintService } from '../services/sprint.service'
import { ChecklistService } from '../services/checklist.service'
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router'
import { Questions } from '../models/questions'
import { Sprint } from '../models/sprint'
import { Project } from '../models/project'
import { ChecklistType } from '../models/checklist_type'


@Component({
  selector: 'app-project-new',
  templateUrl: './project-new.component.html',
  providers: [SprintService, ProjectService, QuestionsService, ChecklistService]
})
export class ProjectNewComponent implements OnInit {

  public projectName: string;
  public projectVersion: string;
  public projectDescription: string;
  public projectID: number;
  public sprintID: number;
  public sprintName: string;
  public sprintDescription: string;
  public questions: Questions[];
  public sprintStore: Sprint[] = [];
  public project: Project[];
  public type = "info"
  public isvalid = false;
  public level: string;
  public error: string[] = [];
  public errors: string;
  public return: boolean = true;
  public checklistType: ChecklistType[]=[];
  public checklistTypeID: number;


  constructor(
    private projectService: ProjectService,
    private sprintService: SprintService,

    private questionsService: QuestionsService,
    private checklistService: ChecklistService,
    private router: Router
  ) { }

  ngOnInit() {

    this.checklistTypeList();
  }

  levelSelect(option: string) {
    this.level = option;

  }
  save() {
    this.return = true;
    this.error = [];

    if (!this.projectName) { this.error.push("Project name was left empty"); this.return = false; }
    if (!this.projectVersion) { this.error.push("Project version was left empty"); this.return = false; }
    if (!this.projectDescription) { this.error.push("Project description was left empty"); this.return = false; }
    if (!this.sprintName) { this.error.push("Sprint name was left empty"); this.return = false; }
    if (!this.sprintDescription) { this.error.push("Sprint description was left empty"); this.return = false; }
    
    if (this.return == false) { return; }

    //This is for getting the sprint items from local storage
    let sprint_items = JSON.parse(localStorage.getItem("questions"));
    let count_sprint = Object.keys(sprint_items).length

      this.sprintService.newSprint(this.sprintName, this.projectID, this.sprintDescription)
        .subscribe(res => { this.sprintID = res['sprintID'] }, error => console.log("error storing sprint"), () => {

          for (let i = 1; i < count_sprint + 1; i++) {
            if (sprint_items["answer" + i] == '0') {  
              this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": Number(sprint_items["answer" + i]), "result": "False", "sprintID": this.sprintID });
            }
            if (sprint_items["sanswer" + i] == '') {  
              this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": Number(sprint_items["answer" + i]), "result": "False", "sprintID": this.sprintID });
            }
            if (sprint_items["answer" + i] != '0') {  
              this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": Number(sprint_items["answer" + i]), "result": "True", "sprintID": this.sprintID });
            }
          }
        });


    setTimeout(() => {

      this.questionsService.newSprint(this.sprintStore, this.checklistTypeID).subscribe(() => { },
        err => console.log("Error Storing new questions for sprint"));
      if (!this.sprintID) { this.router.navigate(['undefined']) }
      else {
        this.router.navigate(['project-dashboard/' + this.projectID]);
      }
    }, 1000);
  }

  //Temp storage for sprint questionaire
  storeSprint(form: NgForm) {
    localStorage.setItem("questions", JSON.stringify(form.value));
    return true;
  }

    selectQuestions(){
      this.questionsService.getQuestions(this.checklistTypeID).subscribe(
        questions => this.questions = questions,
        err => console.log("getting questions failed")
      )
  }

  checklistTypeList() {
    this.checklistService
      .getChecklistTypeList()
      .subscribe(
        checklistType => {
          this.checklistType = checklistType;
          if (!this.checklistType) {
            this.errors = "There are no checklist types defined yet"
          }
        },
        err => this.errors = "Getting the checklist types failed, contact an administrator! ");
  }
  isInvalid() {
    return true;
  }
}