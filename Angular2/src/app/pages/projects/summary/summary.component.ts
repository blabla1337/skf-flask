import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

import { SprintService } from '../../../core/services/sprint.service';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss']
})
export class SummaryComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean;
  private sub: any;
  private id: number;
  public sprintData: any;

  constructor(
    private modalService: NgbModal,
    private route: ActivatedRoute,
    private _sprintService: SprintService,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Sprint result' }, { label: 'Summary', active: true }];
    this.getSprintItems();
  }


  getSprintItems()
  {
    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this._sprintService.getSprintChecklistResults(this.id).subscribe(sprint => this.sprintData = sprint)
  }

  /**
   * Open modal
   * @param content modal content
   */
  summaryModal(content: any)
  {
    this.modalService.open(content, { size: 'lg', centered: true });
  }

  onSubmit()
  {
    this.router.navigate(['/projects/summary']);
  }
}
