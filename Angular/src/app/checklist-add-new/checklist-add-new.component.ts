import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ActivatedRoute, Router } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { QuestionsService } from '../services/questions.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { Checklist } from '../models/checklist';
import { Knowledgebase } from '../models/knowledgebase';
import { Questions } from '../models/questions'


@Component({
  selector: 'app-checklist-add-new',
  templateUrl: './checklist-add-new.component.html',
providers: [ChecklistService, QuestionsService]
})
export class ChecklistAddNewComponent implements OnInit {

  constructor(
    private _checklistService: ChecklistService,

    private _knowledgeService: KnowledgebaseService,
    private _questionsService: QuestionsService,
    private modalService: NgbModal,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  public checklistTypeFromUrl: string;
  public error: string;
  public errors = [];
  public return: boolean;
  public delete:string;
  public succes: string;
  public cwe: number;
  public canEdit: boolean;
  public knowledgebaseID: number;
  public checklist: Checklist[]
  public questions: Questions[] = [];
  public include_always: string;
  public question: number;
  public checklistID: number;
  public content: string;
  public editChecklist: boolean;
  knowledgebaseItems: Knowledgebase[];
  public kbItem: any = {
    "kbID": '',
    "title": ''
  };

  public questionSprint: any = {
    "checklist_type": '',
    "id": '',
    "question": ''
  };

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.checklistTypeFromUrl = params['id'];
      localStorage.setItem("tempParamID", params['id'])
    });
    
    this.checklistTypeFromUrl = localStorage.getItem("tempParamID");
    if (AppSettings.AUTH_TOKEN) {
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes("edit");
    }

    this.getKnowledgeItems();
    this.getQuestionList(Number(localStorage.getItem("tempParamID")));

    /* 
    Put getting the checklist in delay. Otherwise when updating the checklist items the item is fetched before
    the database is updated!
    */
    setTimeout(() => {
    this.getChecklistList();
  }, 1000);
  }

  storeChecklistItem(){
    this.errors = [];  
    this.return = true;

    if (!this.checklistTypeFromUrl) {
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

    if (this.return == false) {
      return;
    }

    this._checklistService.newChecklistItem(Number(this.checklistTypeFromUrl), this.checklistID, this.content, Number(this.kbItem.kbID), this.include_always, Number(this.questionSprint.id), Number(this.cwe))
      .subscribe(
        () => this.getChecklistList(),
        () => this.errors.push("Error storing checklist item, potential duplicate checklist ID")
      );
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(knowledgebaseItems => {
        this.knowledgebaseItems = knowledgebaseItems;
        this.knowledgebaseItems.unshift({
          "kbID": '0',
          "title": 'Use this for a Control Header'
        });
      },
      err => this.error = "Error getting knowledge items, contact the administrator!"
    );
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

  getQuestionList(checklistType:number){
    this._questionsService.getQuestions(checklistType).subscribe(
      sprints => {
        this.questions = sprints;
        this.questions.unshift({
          "checklist_type": '',
          "id": 0,
          "question": 'Empty'
        });
      },
      err => {
        console.log("getting sprint questions failed");
      }
    )
  }

  back() {
    this.router.navigate(["/checklist-manage/"+this.checklistTypeFromUrl]);
  }

  newChecklistItemModal(modalValue) {
    this.modalService.open(modalValue, { size: 'lg' })
    this.readItem()
  }

  readItem() {
    this.editChecklist = false;
    this.checklistID = null;
    this.content = null;

    this.questionSprint = {
      "checklist_type": '',
      "id": '',
      "question": ''
    };
    this.kbItem = {
      "kbID": '',
      "title": ''
    };
    this.include_always = null;
    this.cwe = null;
  }
}
