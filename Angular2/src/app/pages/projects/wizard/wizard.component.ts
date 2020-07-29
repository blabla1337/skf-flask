import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { FormBuilder, FormGroup, Validators, FormArray } from '@angular/forms';

import { ChecklistCategoryService } from '../../../core/services/checklist_category.service';
import { QuestionService } from '../../../core/services/question.service';
import { ChecklistService } from '../../../core/services/checklists.service';
import { SprintService } from '../../../core/services/sprint.service';

@Component({
  selector: 'app-wizard',
  templateUrl: './wizard.component.html',
  styleUrls: ['./wizard.component.scss']
})
export class WizardComponent implements OnInit
{

  project_id = Number(localStorage.getItem("project_id"))
  selected: string;
  categoryData: any;
  questionData: any;
  sprintData: any;
  maturityData = [{ "id": 1, "title": "Level 1" }, { "id": 2, "title": "Level 2" }, { "id": 3, "title": "Level 3" }]
  checklistData: any;
  breadCrumbItems: Array<{}>;
  isSubmitted: boolean;
  newSprintForm: FormGroup;
  sprint_id: number;
  sprintStore: any[];

  questions = new FormArray([]);

  constructor(
    private _checklistCategoryService: ChecklistCategoryService,
    private _questionService: QuestionService,
    private _checklistService: ChecklistService,
    private _sprintService: SprintService,
    private formBuilder: FormBuilder,
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Projects' }, { label: 'Wizard', active: true }];

    this.newSprintForm = this.formBuilder.group({
      name: ['', Validators.required, { disabled: true }],
      description: ['', Validators.required],
      project_id: [],
    })
    this.selected = '';
    this.getCategories()
    this.selectSprints();
  }

  onChange(value)
  {
    this.selected = value;
  }

  getCategories()
  {
    this._checklistCategoryService.getChecklistCategoryCollection().subscribe(data => this.categoryData = data);
  }

  selectChecklistsOnChange(category_id: number)
  {
    this._checklistService.getChecklistsCollection(category_id).subscribe(checklist => this.checklistData = checklist);
  }

  selectQuestionaireOnChange(checklist_id: number)
  {
    this._questionService.getQuestionCollection(checklist_id).subscribe(question => this.questionData = question);
  }

  selectSprints()
  {
    this._sprintService.getSprintsCollection(this.project_id).subscribe(sprint => this.sprintData = sprint)
  }

  selectMaturityOnChange(maturity_id: number)
  {
    localStorage.removeItem("maturity")
    localStorage.setItem("maturity", maturity_id.toString());
  }

  storeSprintLocalStorage()
  {
    //localStorage.setItem('questions', JSON.stringify(form.value));
    return
  }

  storeSprint()
  {
    this.isSubmitted = true;
    if (this.newSprintForm.invalid) {
      return;
    }
    this.newSprintForm.patchValue({ project_id: this.project_id })
    this._sprintService.createSprint(this.newSprintForm.value).subscribe(sprint =>
    {
      localStorage.removeItem("sprint_id")
      localStorage.setItem("sprint_id", sprint['sprint_id'])
    })
  }

  oldSprint(sprint_id: number)
  {
    localStorage.removeItem("sprint_id")
    localStorage.setItem("sprint_id", sprint_id.toString())
  }
}
