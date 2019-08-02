import { Component, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { SprintService } from '../services/sprint.service'
import { CommentService } from '../services/comment.service'
import { Sprint } from '../models/sprint'
import { Comment } from '../models/comment'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

@Component({
  selector: 'app-project-summary',
  templateUrl: './project-summary.component.html',
  providers: [SprintService, CommentService]
})
export class ProjectSummaryComponent implements OnInit {

  constructor(
    private sprintService: SprintService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  public sprintResult: Sprint[];
  public comment: string;
  public checklistID: string;
  public comments: Comment;
  public error: string;
  public succes: string;
  public selector = 'Development';
  public backID: string;
  public showMe: string;
  public canEdit: boolean;

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.sprintService.getSprintResults(params['id']).subscribe(
        resp => this.sprintResult = resp,
        err => console.log('Error getting sprint stats'))
    });
    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes('edit');
    }
  }

  back() {
    this.router.navigate(['/project-dashboard/', localStorage.getItem('project_id')]);
  }

  select(option: string) {
    this.selector = option;
  }
}
