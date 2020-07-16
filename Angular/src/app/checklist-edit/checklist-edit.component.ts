import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { QuestionsService } from '../services/questions.service'

import { Checklist } from '../models/checklist';
import { Knowledgebase } from '../models/knowledgebase';
import { Questions } from '../models/questions';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-checklist-edit',
  templateUrl: './checklist-edit.component.html',
  providers: [ChecklistService, QuestionsService]
})
export class ChecklistEditComponent implements OnInit
{

  constructor(
    private checklistService: ChecklistService,
    private knowledgeService: KnowledgebaseService,
    private questionsService: QuestionsService,
    private modalService: NgbModal,
    private route: ActivatedRoute,
    private router: Router,
    private formBuilder: FormBuilder
  )
  {
  }


  public delete: string;
  public checklistForm: FormGroup;
  public checklistItem: Observable<Checklist>;
  public checklist: Checklist[];
  public questions: Questions[];
  public knowledgebaseItems: Knowledgebase[];
  public knowledgeByFind: Knowledgebase[];
  public isSubmitted: boolean;

  get formControls() { return this.checklistForm.controls; }

  ngOnInit()
  {

    this.route.params.subscribe(params => { localStorage.setItem('checklist_ref_id', params['id']); });

    this.checklistForm = this.formBuilder.group({
      checklist_id: [{ value: '', disabled: true }, [Validators.required, Validators.pattern(/^[0-9]{1,2}([.][0-9]{1,2})?$/)]],
      kb_id: ['', Validators.required],
      question_id: ['', Validators.required],
      include_always: ['', Validators.required],
      content: ['', Validators.required],
      maturity: ['', [Validators.required, Validators.pattern("^[0-9]*$")]],
    })

    this.getKnowledgeItems();
    this.getQuestionList();
    setTimeout(() =>
    {
      this.getChecklistItem();
    }, 200);
  }

  updateChecklistItem()
  {
    this.isSubmitted = true;
    if (this.checklistForm.invalid) {
      return;
    }
    this.checklistService.updateChecklistItem(localStorage.getItem('checklist_ref_id'), Number(localStorage.getItem('checklist_type_id')), this.checklistForm.value)
      .subscribe(
        () => this.back(),
        () => console.log('Error updating checklist item, potential duplicate or incorrect checklist ID (1.2, 1.2, 2.1, etc)')
      );
    this.router.navigate(['/checklist-add-new/', localStorage.getItem('checklist_type_id')]);

  }

  getKnowledgeItems()
  {
    let category_id = localStorage.getItem("category_id");
    this.knowledgeService.getKnowledgeBase(Number(category_id)).subscribe(knowledgebaseItems =>
    {
      this.knowledgebaseItems = knowledgebaseItems;
    },
      err => console.log('Error getting knowledge items, contact the administrator!')
    );
  }

  getChecklistItem()
  {
    this.checklistService.getSingleChecklistItem(localStorage.getItem('checklist_ref_id'), Number(localStorage.getItem('checklist_type_id'))).subscribe(checklist =>
    {
      this.checklist = checklist;
    },
      err => console.log('Error getting checklist items, contact the administrator!')
    );

    setTimeout(() =>
    {
      //check if questio was None otherwise give it the id/content previously selected!
      if (this.checklist['question_id'] == null) {
        var question_id = {
          'id': 0,
          'question': 'None'
        }
      } else {
        question_id = {
          'id': this.checklist['question_id'],
          'question': this.checklist['questions']
        }
      }
      //check if knowledgebase item was None otherwise give it the id/content previously selected!
      var kb_item = {
        'kb_id': this.checklist['kb_id'],
        'title': this.checklist['kb_title']
      };
      this.checklistForm.patchValue({
        checklist_id: this.checklist['checklist_id'],
        kb_id: kb_item,
        question_id: question_id,
        include_always: this.checklist['include_always'],
        content: this.checklist['content'],
        add_resources: this.checklist['add_resources'],
        maturity: this.checklist['maturity'],
      });
    }, 100);
  }

  getQuestionList()
  {
    this.questionsService.getQuestions(Number(localStorage.getItem('checklist_type_id'))).subscribe(questions =>
    {
      this.questions = questions;
      this.questions.unshift({
        'id': '0',
        'question': 'None'
      });
    },
      err => console.log('Error getting question items, contact the administrator!')
    );
  }


  back()
  {
    this.router.navigate(['/checklist-add-new/', localStorage.getItem('checklist_type_id')]);
  }

  deleteChecklistItem()
  {
    if (this.delete == 'DELETE') {
      this.checklistService.deletechecklistItem(localStorage.getItem('checklist_ref_id'), Number(localStorage.getItem('checklist_type_id'))).subscribe(x =>
        this.router.navigate(['/checklist-add-new/', localStorage.getItem('checklist_type_id')]));
      this.delete = '';
    }
  }

  deleteChecklistItemModal(modalValue)
  {
    this.modalService.open(modalValue, { size: 'lg' })
  }
}
