import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';

import { KnowledgebaseService } from '../../../core/services/knowledgebase.service';
@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateComponent implements OnInit
{

  breadCrumbItems: Array<{}>;
  public knowledgebaseForm: FormGroup;

  public submit: boolean;
  public formsubmit: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private _knowledgebaseService: KnowledgebaseService
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'Create', active: true }];

    this.knowledgebaseForm = this.formBuilder.group({
      title: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      content: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
    });
    this.submit = false;
  }

  createKnowledgebaseItem()
  {
    this.submit = true;
    if (this.knowledgebaseForm.invalid) {
      return;
    }
    this._knowledgebaseService.createKnowledgebaseItem(this.knowledgebaseForm.value).subscribe(() => this.router.navigate(['/knowledgebase/view']))
  }


  get form()
  {
    return this.knowledgebaseForm.controls;
  }

  validSubmit()
  {
    this.submit = true;
  }
}
