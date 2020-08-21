import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-update',
  templateUrl: './update.component.html',
  styleUrls: ['./update.component.scss']
})
export class UpdateQuestionnaireComponent implements OnInit
{

  // Bread crumb item
  breadCrumbItems: Array<{}>;

  constructor() { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Questionnaire' }, { label: 'Update', active: true }];
  }

}
