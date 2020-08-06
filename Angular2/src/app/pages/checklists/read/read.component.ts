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
  value: number;
  private sub: any;

  // Collapse value
  public isCollapsed: boolean[] = [];

  constructor(
    private modalService: NgbModal,
    // tslint:disable-next-line: variable-name
    private _checklistCategoryService: ChecklistService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Checklists' }, { label: 'Read', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      // tslint:disable-next-line: no-string-literal
      this.id = +params['id'];
      localStorage.setItem('controlSelector', this.id.toString())
    });

    // this is hardcoded refactor this to make it work better

    this.getChecklistColletion();
    this.value = Number(localStorage.getItem('categorySelector'));
    if (this.value === 1) {
      this.getChecklistControls(1);
    } else if (this.value === 2) {
      this.getChecklistControls(15);
    } else {
      this.getChecklistControls(18);
    }
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
    this.router.navigate(['/checklists/read', id]);
  }

  changeControlsOnSelect(id: number)
  {
    this.getChecklistControls(id);
    this.router.navigate(['/checklists/read', id]);
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any)
  {
    this.modalService.open(centerDataModal, { centered: true });
  }

  // tslint:disable-next-line: variable-name
  storeSprintLocalStorage(sprint_id: number)
  {
    // localStorage.setItem('questions', JSON.stringify(form.value));
    return;
  }



}
