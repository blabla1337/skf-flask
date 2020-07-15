import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-edit',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  constructor(private router: Router) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'Edit', active: true }];
  }

  onUpdate() {
    this.router.navigate(['/code-example/view']);
  }

  onCancel() {
    this.router.navigate(['/code-example/view']);
  }
}
