import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service'
import { QuestionService } from '../../../core/services/question.service'
import { ChecklistService } from '../../../core/services/checklists.service'



@Component({
  selector: 'app-add-requirement',
  templateUrl: './add-requirement.component.html',
  styleUrls: ['./add-requirement.component.scss']
})
export class AddRequirementComponent implements OnInit
{

  public breadCrumbItems: Array<{}>;
  public validationform: FormGroup;
  public typeValidationForm: FormGroup;
  public submit: boolean;
  public questionData: any = [];
  public knowledgeData: any = [];
  public include_always: any = [];
  public categoryId = Number(localStorage.getItem("categorySelector"));
  public checklistId = Number(localStorage.getItem("checklist_id"));
  public routerId;
  constructor(
    private _knowledgebaseSerice: KnowledgebaseService,
    private _questionService: QuestionService,
    private _checklistService: ChecklistService,
    private formBuilder: FormBuilder,
    private router: Router,
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Add requirements', active: true }];

    this.validationform = this.formBuilder.group({
      checklist_id: ['', [Validators.required]],
      content: ['', [Validators.required]],
      include_always: ['False', [Validators.required]],
      kb_id: ['Please select knowledgebase item', [Validators.required]],
      maturity: ['', [Validators.required]],
      question_id: ['Please select question', [Validators.required]],
      add_resources: ['', [Validators.required]]
    });

    this.submit = false;
    this.include_always = ['True', 'False']
    this._fetchData();
  }

  _fetchData()
  {
    this._knowledgebaseSerice
      .getKnowledgeBaseItemsCollection(this.categoryId)
      .subscribe(items => this.knowledgeData = items);

    this._questionService
      .getQuestionCollection(this.checklistId)
      .subscribe(question =>
      {
        this.questionData = question;
        this.questionData.items.unshift({
          'id': 0,
          'question': 'Empty',
          'checklist_type': 0,
        });
      });
  }

  storeChecklistItem()
  {
    this.submit = true;
    if (this.validationform.invalid) {
      return;
    }

    this.validationform.patchValue({
      kb_id: this.validationform.value['kb_id']['kb_id'],
      question_id: this.validationform.value['question_id']['id'],
      maturity: Number(this.validationform.value['maturity'])
    });

    this._checklistService
      .createChecklistItem(this.validationform.value, this.checklistId)
      .subscribe(() => this.router.navigate(['/checklists/manage', this.checklistId]));
  }
  get form()
  {
    return this.validationform.controls;
  }

  validSubmit()
  {
    this.submit = true;
  }
}
