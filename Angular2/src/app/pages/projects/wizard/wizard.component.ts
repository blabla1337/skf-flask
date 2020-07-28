import { Component, OnInit } from '@angular/core';

import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';
import { QuestionService } from '../../../core/services/question.service';
import { ChecklistService } from '../../../core/services/checklists.service';

@Component({
  selector: 'app-wizard',
  templateUrl: './wizard.component.html',
  styleUrls: ['./wizard.component.scss']
})
export class WizardComponent implements OnInit
{

  selected: string;
  categoryData: any;
  questionData: any;
  maturityData = [{ "id": 1, "title": "Level 1" }, { "id": 2, "title": "Level 2" }, { "id": 3, "title": "Level 3" }]
  checklistData: any;
  breadCrumbItems: Array<{}>;

  constructor(
    private _checklistCategoryService: ChecklistCategoryService,
    private _questionService: QuestionService,
    private _checklistService: ChecklistService
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Wizard', active: true }];

    this.selected = '';
    this.getCategories()
  }

  getCategories()
  {
    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);
  }

  selectMaturityOnChange(maturity_id: number)
  {
    localStorage.removeItem("maturity")
    localStorage.setItem("maturity", maturity_id.toString())
  }

  selectChecklistsOnChange(category_id: number)
  {
    this._checklistService.getChecklistsCollection(category_id).subscribe(checklist => this.checklistData = checklist)
  }

  selectQuestionaireOnChange(checklist_id: number)
  {
    this._questionService.getQuestionCollection(checklist_id).subscribe(question => this.questionData = question)
  }


}
