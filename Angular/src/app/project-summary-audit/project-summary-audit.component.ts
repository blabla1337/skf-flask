import { Component, OnInit } from '@angular/core';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { SprintService } from '../services/sprint.service'
import { CommentService } from '../services/comment.service'
import { Sprint } from '../models/sprint'
import { Comment } from '../models/comment'

@Component({
  selector: 'app-project-summary-audit',
  templateUrl: './project-summary-audit.component.html',
  providers: [SprintService, CommentService]
})
export class ProjectSummaryAuditComponent implements OnInit {

  constructor(
    private sprintService: SprintService,
    private commentService: CommentService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  public sprintResult: Sprint[];
  public comment: string;
  public checklistID: string;
  public comments: Comment;
  public error: string;
  public succes: string;
  public selector: string = "Development";
  public showMe: string;

  ngOnInit() {
    this.route.params.subscribe(params => {
      this.sprintService.getSprintResultsAudit(params["id"]).subscribe(
        resp => this.sprintResult = resp,
        err => console.log("Error getting sprint stats"))
    });
  }

  back() {
    this.route.params.subscribe(params => { this.router.navigate(["/project-dashboard/", localStorage.getItem("tempParamID")]) })
  }

  export() {
    this.route.params.subscribe(params => { this.sprintService.getSprintResultsAuditExport(params["id"]).subscribe(
      (resp) => {
        let base64fix = resp.replace("b'", "");
        const base64 = base64fix.substring(0, base64fix.lastIndexOf("'"));

        let a = document.createElement("a");
        document.body.appendChild(a);

        const byteCharacters = atob(base64);
        let byteArrays = [];

        for (let offset = 0; offset < byteCharacters.length; offset += 512) {
          let slice = byteCharacters.slice(offset, offset + 512);

          let byteNumbers = new Array(slice.length);
          for (var i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
          }

          let byteArray = new Uint8Array(byteNumbers);

          byteArrays.push(byteArray);
        }

        const blob = new Blob(byteArrays, {type: "text/csv"});
        const url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = "export.csv";
        a.click();
        window.URL.revokeObjectURL(url);
      },
      err => console.log("Error getting sprint stats")
    ); });
  }

  select(option: string) {
    this.selector = option;
  }

  save(status: number, checklist: string) {
    this.route.params.subscribe(params => {
      this.commentService.newComment(checklist, this.comment, params['id'], status).subscribe(
        () => { },
        err => this.succes = "nonono",
        () => { this.succes = "comment was added to trail"; }
      )
    });

    this.route.params.subscribe(params => {
      this.sprintService.getSprintResultsAudit(params['id']).subscribe(
        resp => this.sprintResult = resp,
        err => console.log("Error getting sprint stats"))
    });
  }

  fetchComment(checklistId) {
    this.error = "";
    this.succes = "";
    this.comment = "";
    this.showMe = checklistId;
    this.route.params.subscribe(params => {
      this.commentService.getComment(checklistId, params['id']).subscribe(
        (data) => {
          this.comments = data;
          if (!this.comments) {
            this.error = "There are no comments available yet!";
          }
        },
        err => console.log("Error whilst getting the comment!")
      )
    });
  }
}


