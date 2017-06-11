import { Component, OnInit } from '@angular/core';
import { ProjectService } from '../services/project.service'
import { QuestionPreService } from '../services/questions-pre.service'
import { QuestionsSprintService } from '../services/questions-sprint.service'
import { SprintService } from '../services/sprint.service'
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router'
import { Question_pre } from '../models/question_pre'
import { Question_sprint } from '../models/question_sprint'
import { Sprint } from '../models/sprint'
import { Project } from '../models/project'

@Component({
  selector: 'app-project-new',
  templateUrl: './project-new.component.html',
  providers: [SprintService, ProjectService, QuestionPreService, QuestionsSprintService]
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
  public level :string;
  public error: string[] = [];
  public return: boolean = true;

  constructor(
    private projectService: ProjectService,
    private sprintService: SprintService,
    private questionPreService: QuestionPreService,
    private questionsSprintService: QuestionsSprintService,
    private router: Router
  ) { }

  ngOnInit() {

    this.questionPreService.getPreQuestions().subscribe(
      questions => this.pre_dev = questions,
      err => console.log("getting pre dev questions failed")
    )

    this.questionsSprintService.getSprintQuestions().subscribe(
      questions => this.sprints = questions,
      err => console.log("getting sprint questions failed")
    )
  }

  levelSelect(option:string){
    this.level = option;
    console.log("aaa")
  }
  save(): void {
    this.return = true;
    this.error = [];
    if (!this.projectName) { this.error.push("Project name was left empty"); this.return = false; }
    if (!this.projectVersion) { this.error.push("Project version was left empty"); this.return = false; }
    if (!this.projectDescription) { this.error.push("Project description was left empty"); this.return = false; }
    if (!this.sprintName) { this.error.push("Sprint name was left empty"); this.return = false; }
    if (!this.sprintDescription) { this.error.push("Sprint description was left empty"); this.return = false; }
    if (!this.level) { this.error.push("No ASVS level was selected"); this.return = false; }

    if (this.return == false) { return; }

    //This is for storing the sprint items from local storage
    let sprint_items = JSON.parse(localStorage.getItem("sprint"));
    let count_sprint = Object.keys(sprint_items).length

    //This is for storing the pre dev items from local storage
    let pre_dev_items = JSON.parse(localStorage.getItem("pre_dev"));
    let count_pre = Object.keys(pre_dev_items).length

    this.projectService.newProject(this.projectName, this.projectVersion, this.projectDescription, this.level)
      .subscribe((res) => { this.projectID = res["projectID"] }, err => console.log("Error storing project"), () => {
        this.sprintService.newSprint(this.sprintName, this.projectID, this.sprintDescription)
          .subscribe(res => { this.sprintID = res['sprintID'] }, error => console.log("error storing sprint"), () => {

            for (let i = 1; i < count_pre + 1; i++) {
              if (pre_dev_items["pre_dev_answer" + i].toString() == "") { pre_dev_items["pre_dev_answer" + i] = "False"; }
              this.pre_dev_store.push({ "projectID": this.projectID, "question_pre_ID": i, "result": pre_dev_items["pre_dev_answer" + i].toString() });
            }

            for (let i = 1; i < count_sprint + 1; i++) {
              if (sprint_items["sprint_answer" + i].toString() == "") { sprint_items["sprint_answer" + i] = "False"; }
              this.sprintStore.push({ "projectID": this.projectID, "question_sprint_ID": i, "result": sprint_items["sprint_answer" + i].toString(), "sprintID": this.sprintID });
            }
          })
      });

    setTimeout(() => {
      this.questionPreService.newProject(this.pre_dev_store).subscribe(() => { },
        err => console.log("Error Storing pre development questions"));

      this.questionsSprintService.newSprint(this.sprintStore).subscribe(() => { },
        err => console.log("Error Storing new questions for sprint"));

      this.router.navigate(['project-dashboard/' + this.projectID]);
      
    }, 1000);

  }

  //Temp storage for pre development questionaire
  storePre(form: NgForm) {
    localStorage.setItem("pre_dev", JSON.stringify(form.value));
  }

  //Temp storage for sprint questionaire
  storeSprint(form: NgForm) {
    localStorage.setItem("sprint", JSON.stringify(form.value));
  }

  isInvalid() {
    return true;
  }
}