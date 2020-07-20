import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

@Component({
  selector: 'app-summary',
  templateUrl: './summary.component.html',
  styleUrls: ['./summary.component.scss']
})
export class SummaryComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Collapse value
  public isCollapsed: boolean;

  constructor(private modalService: NgbModal,
              private router: Router) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Summary', active: true }];
  }

  /**
   * Open modal
   * @param content modal content
   */
 summaryModal(content: any) {
  this.modalService.open(content, { size: 'lg', centered: true });
}

onSubmit() {
  this.router.navigate(['/projects/summary']);
}
}
