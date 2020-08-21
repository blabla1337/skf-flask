import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateQuestionnaireComponent implements OnInit
{

  // Bread crumb item
  breadCrumbItems: Array<{}>;

  constructor() { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Questionnaire' }, { label: 'Create', active: true }];
  }

}
