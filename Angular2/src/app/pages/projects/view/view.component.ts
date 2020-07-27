import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute } from '@angular/router';

import { SprintService } from '../../../core/services/sprint.service';

@Component({
  selector: 'app-view',
  templateUrl: './view.component.html',
  styleUrls: ['./view.component.scss']
})
export class ProjectViewComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  id: number;
  private sub: any;
  sprintData: any;
  selected: string;

  constructor(
    private modalService: NgbModal,
    private _sprintService: SprintService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Features' }, { label: 'View', active: true }];
    this.getSprintItems()

  }


  getSprintItems()
  {
    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this._sprintService.getSprintsCollection(this.id).subscribe(sprint => this.sprintData = sprint)
  }

  projectCreate()
  {
    this.router.navigate(['/projects/wizard']);
  }

  onView(id: number)
  {
    this.router.navigate(['/projects/summary', id]);
  }

}
