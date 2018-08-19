import { Component } from '@angular/core';
import { ChecklistService } from '../services/checklist.service'
import { Checklist } from '../models/checklist';
import { StartsWithPipe } from '../pipes/starts-with.pipe'
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { OrderBy } from '../pipes/order-by.pipe'


@Component({
  selector: 'app-checklist',
  templateUrl: './checklist.component.html',
  providers: [ChecklistService],
})

export class ChecklistComponent {
  public checklistItems: Checklist[]
  public queryString: string;
  public closeResult: string;
  public level: number;
  public checklist_type: number;
  public color: string;

  constructor(private checklistService: ChecklistService, private modalService: NgbModal) { }

  open(content, level: number, checklist_type: number) {
    this.level = level;
    this.checklist_type = checklist_type;
    this.checklistService
      .getChecklist(level, checklist_type)
      .subscribe(checklistItems => { this.checklistItems = checklistItems });
      this.modalService.open(content, { size: 'lg' })
  }
}
