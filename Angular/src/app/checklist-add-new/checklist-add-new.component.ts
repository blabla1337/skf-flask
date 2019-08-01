import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ActivatedRoute, Router } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { QuestionsService } from '../services/questions.service'
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
    private router: Router,
    private formBuilder: FormBuilder
  ) { }

  public checklistForm: FormGroup;
  public isSubmitted: boolean;
  public checklistTypeFromUrl: string;
  public checklist: Checklist[]
  public questions: Questions[] = [];
  public knowledgebaseItems: Knowledgebase[];
  get formControls() { return this.checklistForm.controls; }
  
  public kbItem: any = {
    'kbID': '',
    'title': ''
  };

  public questionSprint: any = {
    'checklist_type': '',
    'id': '',
    'question': ''
  };

  ngOnInit() {

    this.checklistForm = this.formBuilder.group({
      checklist_id: ['', [Validators.required, Validators.pattern(/^[0-9]{1,2}([.][0-9]{1,2})?$/)]],
      kb_id: ['', Validators.required],
      question_id: ['', Validators.required],
      include_always: ['', Validators.required],
      content: ['', Validators.required],
      cwe: ['', [Validators.required, Validators.pattern("^[0-9]*$")]],
    })

    this.route.params.subscribe(params => {
      this.checklistTypeFromUrl = params['id'];
    });
  
    /*
    Put getting the checklist in delay. Otherwise when updating the checklist items the item is fetched before
    the database is updated!
    */
    setTimeout(() => {
    this.getKnowledgeItems();
    this.getQuestionList(Number(localStorage.getItem('checklist_type_id')));
    this.getChecklistList();
  }, 1000);
  }

  storeChecklistItem() {
    this.isSubmitted = true;
    if(this.checklistForm.invalid){
      return;
    }
    this._checklistService.newChecklistItem(Number(localStorage.getItem('checklist_type_id')), this.checklistForm.value)
      .subscribe(
        () => this.getChecklistList(),
        () => console.log('Error storing checklist item, potential duplicate checklist ID')
      );
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(knowledgebaseItems => {
        this.knowledgebaseItems = knowledgebaseItems;
      },
      (err) => console.log('Error getting knowledge items, contact the administrator!')
    );
  }

  getChecklistList() {
    this._checklistService
      .getChecklistByType(Number(localStorage.getItem('checklist_type_id')))
      .subscribe(
        checklist => {
         this.checklist = checklist;
          if (!this.checklist) {
          console.log('There are no checklist types defined yet')
        }
      }),
      () => console.log('Getting the checklist types failed, contact an administrator! ')
  }

  getQuestionList(checklistType: number) {
    this._questionsService.getQuestions(checklistType).subscribe(
      sprints => {
        this.questions = sprints;
        this.questions.unshift({
          'checklist_type': '',
          'id': 0,
          'question': 'Empty'
        });
      },
      err => {
        console.log('getting sprint questions failed');
      }
    )
  }

  back() {
    this.router.navigate(['/checklist-manage/' + this.checklistTypeFromUrl]);
  }

  newChecklistItemModal(modalValue) {
    this.modalService.open(modalValue, { size: 'lg' })
    this.readItem()
  }

  readItem() {
    this.questionSprint = {
      'checklist_type': '',
      'id': '',
      'question': ''
    };
    this.kbItem = {
      'kbID': '',
      'title': ''
    };
  }
}
