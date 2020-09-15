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
  public id: number;
  private sub: any;
  public sprintData: any;
  public selected: string;
  public queryString;
  public routerId;

  constructor(
    private modalService: NgbModal,
    private _sprintService: SprintService,
    private route: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Features' }, { label: 'Sprints', active: true }];
    this.getSprintItems()
    this.routerId = this.route.snapshot.paramMap.get('id');
    localStorage.setItem('routerId', this.routerId);
  }


  getSprintItems()
  {
    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
      localStorage.setItem("project_id", this.id.toString())
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
