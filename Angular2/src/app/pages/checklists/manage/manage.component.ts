import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { ActivatedRoute } from '@angular/router';

import { QuestionService } from '../../../core/services/question.service'

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
  public questionData: any;


  public checkData: any;

  constructor(
    private _questionService: QuestionService,
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
  }

  getQuestions()
  {
    this._questionService
      .getQuestionCollection(Number(localStorage.getItem("checklist_id")))
      .subscribe(questions => this.questionData = questions)
  }

  deleteQuestion(id: number)
  {
    if (this.delete == 'DELETE') {
      this._questionService.deleteQuestionById(id).subscribe(x => this.getQuestions());
    }
  }

  centerModal(centerDataModal: any)
  {
    this.modalService.open(centerDataModal, { centered: true, size: 'lg' });
  }

}
