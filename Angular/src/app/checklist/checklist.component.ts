import { Component } from '@angular/core';
import { ChecklistService } from '../services/checklist.service'
import { ChecklistType } from '../models/checklist_type';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { Checklist } from '../models/checklist';


@Component({
  selector: 'app-checklist',
  templateUrl: './checklist.component.html',
  providers: [ChecklistService],
})

export class ChecklistComponent {
  public checklistTypes: ChecklistType[] = [];
  public checklistItems: Checklist[] = [];
  public queryString: string;
  public closeResult: string;
  public level: number;
  public error: string;
  public checklist_type: number;
  public color: string;

  constructor(private checklistService: ChecklistService, private modalService: NgbModal) { }


  ngOnInit() {
    this.checklistTypeList()
  }

  checklistTypeList() {
    this.checklistService
      .getChecklistTypeList()
      .subscribe(
        checklistTypes => {
          this.checklistTypes = checklistTypes;
          if (!this.checklistTypes) {
            this.error = 'There are no checklist types defined yet'
          }
        },
        err => this.error = 'Getting the checklist types failed, contact an administrator! ');
  }

  open(content, typeID: number) {
    this.checklistService
      .getChecklistByType(typeID)
      .subscribe(checklistItems => { this.checklistItems = checklistItems });
      this.modalService.open(content, { size: 'lg' })
  }
}
