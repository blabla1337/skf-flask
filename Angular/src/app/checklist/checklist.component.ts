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
  public color: string;

  constructor(private checklistService: ChecklistService, private modalService: NgbModal) { }

  open(content, level: number) {
    this.level = level;
    this.checklistService
      .getChecklist(level)
      .subscribe(checklistItems => { this.checklistItems = checklistItems });
      this.modalService.open(content, { size: 'lg' })
  }
}
