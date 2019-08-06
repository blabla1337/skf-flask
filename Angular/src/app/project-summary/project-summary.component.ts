import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute, Params } from '@angular/router';
import { SprintService } from '../services/sprint.service'
import { Sprint } from '../models/sprint'

@Component({
  selector: 'app-project-summary',
  templateUrl: './project-summary.component.html',
  providers: [SprintService]
})
export class ProjectSummaryComponent implements OnInit {

  constructor(
    private sprintService: SprintService,
    private route: ActivatedRoute,
    private router: Router,
    private modalService: NgbModal
  ) { }

  public sprintResult: Sprint[];
  public delete: string;

  ngOnInit() {
    this.getSprintResults()
  }

  getSprintResults() {
    this.route.params.subscribe(params => {
      this.sprintService.getSprintResults(params['id']).subscribe(
        resp => this.sprintResult = resp,
        () => console.log('Error getting sprint stats'))
    });
  }

  deleteChecklistResult(checklist_result_id: number) {
    if (this.delete == 'DELETE') {
      this.sprintService.deleteChecklistResult(checklist_result_id).subscribe(x =>
        this.getSprintResults())
    }
  }

  deleteModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  back() {
    this.router.navigate(['/project-dashboard/', localStorage.getItem('project_id')]);
  }

  export() {
    this.route.params.subscribe(params => { this.sprintService.getSprintResultsExport(params['id']).subscribe(
      (resp) => {
        const base64fix = resp.replace('b\'', '');
        const base64 = base64fix.substring(0, base64fix.lastIndexOf('\''));

        const a = document.createElement('a');
        document.body.appendChild(a);

        const byteCharacters = atob(base64);
        const byteArrays = [];

        for (let offset = 0; offset < byteCharacters.length; offset += 512) {
          const slice = byteCharacters.slice(offset, offset + 512);

          const byteNumbers = new Array(slice.length);
          for (let i = 0; i < slice.length; i++) {
            byteNumbers[i] = slice.charCodeAt(i);
          }

          const byteArray = new Uint8Array(byteNumbers);

          byteArrays.push(byteArray);
        }

        const blob = new Blob(byteArrays, {type: 'text/csv'});
        const url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = 'export.csv';
        a.click();
        window.URL.revokeObjectURL(url);
      },
      err => console.log('Error getting sprint stats')
    ); });
  }
}
