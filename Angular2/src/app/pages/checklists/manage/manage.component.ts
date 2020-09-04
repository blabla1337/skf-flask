import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ActivatedRoute } from '@angular/router';

import { QuestionService } from '../../../core/services/question.service'
import { ChecklistService } from '../../../core/services/checklists.service'

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class CheckManageComponent implements OnInit
{
  public breadCrumbItems: Array<{}>;
  public isCollapsed: boolean[] = [];
  public id: number;
  public sub: any;
  public delete: string
  public questionData: any = [];
  public checklistData: any = [];
  public correlationData: any = [];
  public selectedQuestion: number;
  public ngbNav;

  public checkData: any;

  constructor(
    private _questionService: QuestionService,
    private _checklistService: ChecklistService,
    private route: ActivatedRoute,
    private modalService: NgbModal
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Manage', active: true }];
    this.sub = this.route.params.subscribe(params =>
    {
      localStorage.setItem("checklist_id", params['id'])
    });
    this.getQuestions()
    this.getChecklistItems()
  }

  getQuestions()
  {
    this._questionService
      .getQuestionCollection(Number(localStorage.getItem("checklist_id")))
      .subscribe(questions => this.questionData = questions)
  }

  getChecklistItems()
  {
    this._checklistService
      .getChecklistItems(Number(localStorage.getItem("checklist_id")))
      .subscribe(checklist => this.checklistData = checklist)
  }

  deleteQuestion(id: number)
  {
    if (this.delete == 'DELETE') {
      this._questionService.deleteQuestionById(id).subscribe(x => this.getQuestions());
    }
  }

  deleteRequirement(id: number)
  {
    if (this.delete == 'DELETE') {
      this._checklistService.deleteChecklistItemById(id).subscribe(x => this.getChecklistItems());
    }
  }

  selectQuestionFromDropDown()
  {
    this._checklistService
      .getChecklistItemsCorrelatedToQuestion(this.selectedQuestion)
      .subscribe(data => this.correlationData = data)
  }

  removeChecklisCorrelation(checklist_id: number)
  {
    this._checklistService
      .updateChecklisteItemCorrelationToQuestion(checklist_id, 0)
      .subscribe(() =>
      {
        this.selectQuestionFromDropDown();
        this.getChecklistItems();
      })
  }

  addChecklistCorrelation(checklist_id: number)
  {
    this._checklistService
      .updateChecklisteItemCorrelationToQuestion(checklist_id, this.selectedQuestion)
      .subscribe(() =>
      {
        this.selectQuestionFromDropDown();
        this.getChecklistItems();
      })
  }

  centerModal(centerDataModal: any)
  {
    this.modalService.open(centerDataModal, { centered: true, size: 'lg' });
  }

}
