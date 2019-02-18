import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { QuestionPreService } from '../services/questions-pre.service'
import { QuestionsSprintService } from '../services/questions-sprint.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import {Checklist} from '../models/checklist';
import {Knowledgebase} from '../models/knowledgebase';
import {Question_pre} from '../models/question_pre';
import {Question_sprint} from '../models/question_sprint';
import {forkJoin} from 'rxjs';
import {map} from 'rxjs/operators';

@Component({
  selector: 'app-checklist-edit',
  templateUrl: './checklist-edit.component.html',
  providers: [ChecklistService, QuestionPreService, QuestionsSprintService]
})
export class ChecklistEditComponent implements OnInit {

  constructor(
    private _checklistService: ChecklistService,
    private _questionsPreService: QuestionPreService,
    private _knowledgeService: KnowledgebaseService,
    private _questionsSprintService: QuestionsSprintService,
    private modalService: NgbModal,
    private route: ActivatedRoute,
    private router: Router,
  ) {
  }

  public checklistTypeFromStorage: string;
  public checklistIDFromUrl: string;
  public error: string;
  public errors = [];
  public return: boolean;
  public delete: string;
  public succes: string;
  public cwe: string;
  public canEdit: boolean;
  public knowledgebaseID: number;
  public checklist: Checklist[];
  public pre_dev: Question_pre[] = [];
  public sprints: Question_sprint[] = [];
  public include_first: string;
  public include_always: string;
  public checklistID: number;
  public content = "Crunching the right data!";
  public editChecklist: boolean;
  knowledgebaseItems: Knowledgebase[];

  public kbItem: any = {
    "kbID": '',
    "title": ''
  };

  public questionPre: any = {
    "checklist_type": '',
    "id": '',
    "question": ''
  };

  public questionSprint: any = {
    "checklist_type": '',
    "id": '',
    "question": ''
  };

  ngOnInit() {

    this.route.params.subscribe(params => {
      this.checklistIDFromUrl = params['id'];
    });

    this.checklistTypeFromStorage = localStorage.getItem("tempParamID");
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes("edit");
    }

    setTimeout(() => {
      this.getKnowledgeItems();

      // Added the Fork Join for service to get the dropdown list and call the checkListItem service
      forkJoin(
        this.getPreQuestionList(Number(localStorage.getItem("tempParamID"))), this.getSprintQuestionList(Number(localStorage.getItem("tempParamID")))
      ).subscribe(
        response => {

          this.pre_dev = response[0];
          this.pre_dev.unshift({
            "checklist_type": '',
            "id": 0,
            "question": 'Empty'
          });

          this.sprints = response[1];
          this.sprints.unshift({
            "checklist_type": '',
            "id": 0,
            "question": 'Empty'
          });
          this.getChecklistItem();
        },
        error => console.log("Error: ", error)
      );

    }, 1000);
  }

  updateChecklistItem() {

    this.errors = [];
    this.return = true;

    if (!this.checklistTypeFromStorage) {
      this.errors.push("Checklist ID was not filled in");
      this.return = false;
    }
    if (!this.checklistID) {
      this.errors.push("Checklist ID validation failed");
      this.return = false;
    }
    if (!this.content) {
      this.errors.push("The checklist item name was not filled in");
      this.return = false;
    }
    if (this.kbItem === null || this.kbItem.kbID === '') {
      this.errors.push("There was no knowledgebase ID selected");
      this.return = false;
    }
    if (!this.include_always) {
      this.errors.push("Include always choice was not made");
      this.return = false;
    }
    if (!this.include_first) {
      this.errors.push("Include first choice was not made");
      this.return = false;
    }

    if (this.return == false) {
      return;
    }

    this.errors = [];
    this._checklistService.updateChecklistItem(Number(this.checklistTypeFromStorage), this.checklistID, this.content, Number(this.kbItem.kbID), this.include_always, this.include_first, Number(this.questionSprint.id), Number(this.questionPre.id))
      .subscribe(
        () => this.getChecklistItem(),
        () => this.errors.push("Error updating checklist item, potential duplicate or incorrect checklist ID (1.2, 1.2, 2.1, etc)")
      );
      this.router.navigate(["/checklist-add-new/", localStorage.getItem("tempParamID")]);
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(knowledgebaseItems => this.knowledgebaseItems = knowledgebaseItems,
      err => this.error = "Error getting knowledge items, contact the administrator!"
    );
  }


  getChecklistItem() {
    this._checklistService
      .getSingleChecklistItem(this.checklistIDFromUrl, Number(this.checklistTypeFromStorage))
      .subscribe(
        checklist => {
          this.content = checklist['checklist_items_content'];
          this.checklistID = checklist['checklist_items_checklistID'];
          this.include_always = checklist['include_always'];
          this.include_first = checklist['include_first'];
          this.cwe = checklist['cwe'];

          this.kbItem = {
            "kbID": checklist['kb_item_id'],
            "title": checklist['kb_item_title']
          };
          this.questionPre = this.getQuestionByFind(this.pre_dev, checklist['question_pre_ID']);
          this.questionSprint = this.getQuestionByFind(this.sprints, checklist['question_sprint_ID']);

          if (!this.checklist) {
            this.error = "There are no checklist types defined yet"
          }
        },
        err => this.error = "Getting the checklist types failed, contact an administrator! ");
  }

  getPreQuestionList(checklistType: number) {
    return this._questionsPreService.getPreQuestions(checklistType);
  }

  getSprintQuestionList(checklistType: number) {
    return this._questionsSprintService.getSprintQuestions(checklistType);
  }

  getQuestionByFind(arr, id) {
    return arr.find(x => x.id === id);
  }

  back() {
    this.router.navigate(["/checklist-add-new/", localStorage.getItem("tempParamID")]);
  }

  deleteChecklistItem() {
    if (this.delete == "DELETE") {
      this._checklistService.deletechecklistItem(Number(this.checklistIDFromUrl), Number(this.checklistTypeFromStorage)).subscribe(x =>
        //Get the new project list on delete 
        this.getChecklistItem())
        this.router.navigate(["/checklist-add-new/", localStorage.getItem("tempParamID")]);
        this.delete = "";
    }
  }

  deleteChecklistItemModal(modalValue) {
    this.modalService.open(modalValue, { size: 'lg' })
  }
}
