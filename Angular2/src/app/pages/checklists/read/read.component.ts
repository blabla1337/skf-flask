import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Router, ActivatedRoute } from '@angular/router';

import { ChecklistService } from '../../../core/services/checklists.service';


@Component({
  selector: 'app-read',
  templateUrl: './read.component.html',
  styleUrls: ['./read.component.scss']
})
export class ChecklistsReadComponent implements OnInit
{

  // Bread crumb item
  breadCrumbItems: Array<{}>;
  public queryString;
  public checklistCatData: any;
  public checklistConData: any;
  id: number;
  private sub: any;

  // Collapse value
  public isCollapsed: boolean[] = [];

  constructor(
    private modalService: NgbModal,
    private _checklistCategoryService: ChecklistService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Read', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
      localStorage.setItem("controlSelector", this.id.toString())
    });

    this.getChecklistColletion();
    this.getChecklistControls(Number(localStorage.getItem('controlSelector')));
  }

  getChecklistColletion()
  {
    this._checklistCategoryService
      .getChecklistsCollection(Number(localStorage.getItem('categorySelector')))
      .subscribe(checklistCat => this.checklistCatData = checklistCat);

  }

  getChecklistControls(id: number)
  {
    this._checklistCategoryService
      .getChecklistsControls(id)
      .subscribe(checklistCon => this.checklistConData = checklistCon);
  }


  changeControlsOnSelect(id: number)
  {
    this.getChecklistControls(id);
    this.router.navigate(['/checklists/read', id])
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) 
  {
    this.modalService.open(centerDataModal, { centered: true });
  }

  storeSprintLocalStorage(sprint_id: number)
  {
    //localStorage.setItem('questions', JSON.stringify(form.value));
    return
  }



}
