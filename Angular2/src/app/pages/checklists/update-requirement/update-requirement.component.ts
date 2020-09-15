import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service'
import { QuestionService } from '../../../core/services/question.service'
import { ChecklistService } from '../../../core/services/checklists.service'

@Component({
  selector: 'app-updaterequirement',
  templateUrl: './update-requirement.component.html',
  styleUrls: ['./update-requirement.component.scss']
})
export class UpdateRequirementComponent implements OnInit
{


  public breadCrumbItems: Array<{}>;
  public validationform: FormGroup;
  public typeValidationForm: FormGroup;
  public submit: boolean;
  public id: number;
  private sub: any;
  public questionData: any = [];
  public knowledgeData: any = [];
  public include_always: any = [];
  public categoryId = Number(localStorage.getItem("categorySelector"))
  public checklistId = Number(localStorage.getItem("checklist_id"))
  public kbitem: string[];


  constructor(
    private _knowledgebaseSerice: KnowledgebaseService,
    private _questionService: QuestionService,
    private _checklistService: ChecklistService,
    private formBuilder: FormBuilder,
    private router: Router,
    private route: ActivatedRoute,
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Update', active: true }];

    this.include_always = ['True', 'False']

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this.validationform = this.formBuilder.group({
      checklist_id: ['', [Validators.required]],
      content: ['', [Validators.required]],
      include_always: ['', [Validators.required]],
      kb_id: ['', [Validators.required]],
      maturity: ['', [Validators.required]],
      question_id: ['', [Validators.required]],
      add_resources: ['', [Validators.required]]
    });

    this.submit = false;
    this._checklistService.getChecklistItemById(this.id).subscribe(item => 
    {

      if (item['question_id'] == null) {
        var question = {
          'id': 0,
          'question': 'None'
        }
      } else {
        question = {
          'id': item['question_id'],
          'question': item['questions']
        }
      }
      // check if knowledgebase item was None otherwise give it the id/content previously selected!
      var kb_item = {
        'kb_id': item['kb_id'],
        'title': item['kb_title']
      };

      this.validationform.patchValue({
        checklist_id: item['checklist_id'],
        kb_id: kb_item,
        content: item['content'],
        question_id: question,
        include_always: item['include_always'],
        maturity: item['maturity'],
        add_resources: item['add_resources']
      });
    });

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

  UpdateChecklistItem()
  {
    this.submit = true;
    if (this.validationform.invalid) {
      return;
    }

    this.validationform.patchValue({
      kb_id: this.validationform.value['kb_id']['kb_id'],
      question_id: this.validationform.value['question_id']['id'],
      maturity: Number(this.validationform.value['maturity'])
    })

    this._checklistService
      .updateChecklistItem(this.validationform.value, this.id)
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
