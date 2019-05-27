import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../services/project.service'
import { QuestionPreService } from '../services/questions-pre.service'
import { QuestionsSprintService } from '../services/questions-sprint.service'
import { SprintService } from '../services/sprint.service'
import { ChecklistService } from '../services/checklist.service'
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router'
import { Question_pre } from '../models/question_pre'
import { Question_sprint } from '../models/question_sprint'
import { Sprint } from '../models/sprint'
import { Project } from '../models/project'
import { ChecklistType } from '../models/checklist_type'


@Component({
  selector: 'app-project-new',
  templateUrl: './project-new.component.html',
  providers: [SprintService, ProjectService, QuestionPreService, QuestionsSprintService, ChecklistService]
})
export class ProjectNewComponent implements OnInit {

  public projectName: string;
  public projectVersion: string;
  public projectDescription: string;
  public projectID: number;
  public sprintID: number;
  public sprintName: string;
  public sprintDescription: string;
  public pre_dev: Question_pre[];
  public pre_dev_store: Question_pre[] = [];
  public sprints: Question_sprint[];
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
    private questionPreService: QuestionPreService,
    private questionsSprintService: QuestionsSprintService,
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
    let sprint_items = JSON.parse(localStorage.getItem("sprint"));
    let count_sprint = Object.keys(sprint_items).length

    //This is for getting the pre dev items from local storage
    let pre_dev_items = JSON.parse(localStorage.getItem("pre_dev"));
    let count_pre = Object.keys(pre_dev_items).length

    //Check if all the fields where set for sprint_items


    this.projectService.newProject(this.projectName, this.projectDescription, Number(this.checklistTypeID), this.projectVersion)
      .subscribe((res) => { this.projectID = res["projectID"] }, err => console.log("Error storing project"), () => {
        this.sprintService.newSprint(this.sprintName, this.projectID, this.sprintDescription)
          .subscribe(res => { this.sprintID = res['sprintID'] }, error => console.log("error storing sprint"), () => {

            for (let i = 1; i < count_pre + 1; i++) {
              if (pre_dev_items["pre_dev_answer" + i] != '0') { 
                  this.pre_dev_store.push({ "projectID": this.projectID, "question_pre_ID": Number(pre_dev_items["pre_dev_answer" + i]), "result": "False" });
              }
              if (pre_dev_items["pre_dev_answer" + i] == '0') { 
                this.pre_dev_store.push({ "projectID": this.projectID, "question_pre_ID": Number(pre_dev_items["pre_dev_answer" + i]), "result": "True" });
              }

              if (pre_dev_items["pre_dev_answer" + i] == '') { 
                this.pre_dev_store.push({ "projectID": this.projectID, "question_pre_ID": Number(pre_dev_items["pre_dev_answer" + i]), "result": "True" });
              }
            }

            for (let i = 1; i < count_sprint + 1; i++) {
              if (sprint_items["sprint_answer" + i] == '0') {  
                this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": Number(sprint_items["sprint_answer" + i]), "result": "False", "sprintID": this.sprintID });
              }
              if (sprint_items["sprint_answer" + i] == '') {  
                this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": Number(sprint_items["sprint_answer" + i]), "result": "False", "sprintID": this.sprintID });
              }
              if (sprint_items["sprint_answer" + i] != '0') {  
                this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": Number(sprint_items["sprint_answer" + i]), "result": "True", "sprintID": this.sprintID });
              }
            }
            console.log(this.sprintStore)
            console.log(this.pre_dev_store)
          })
      });

    setTimeout(() => {
      this.questionPreService.newProject(this.pre_dev_store).subscribe(() => { },
        err => console.log("Error Storing pre development questions"));

      this.questionsSprintService.newSprint(this.sprintStore).subscribe(() => { },
        err => console.log("Error Storing new questions for sprint"));
      if (!this.sprintID) { this.router.navigate(['undefined']) }
      else {
        this.router.navigate(['project-dashboard/' + this.projectID]);
      }
    }, 1000);
  }

  //Temp storage for pre development questionaire
  storePre(form: NgForm) {
    localStorage.setItem("pre_dev", JSON.stringify(form.value));
    return true;
  }

  //Temp storage for sprint questionaire
  storeSprint(form: NgForm) {
    localStorage.setItem("sprint", JSON.stringify(form.value));
    return true;
  }

    selectQuestions(){
      this.questionPreService.getPreQuestions(this.checklistTypeID).subscribe(
        questions => this.pre_dev = questions,
        err => console.log("getting pre dev questions failed")
      )
  
      this.questionsSprintService.getSprintQuestions(this.checklistTypeID).subscribe(
        questions => this.sprints = questions,
        err => console.log("getting sprint questions failed")
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