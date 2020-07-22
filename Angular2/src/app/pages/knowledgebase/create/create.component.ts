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

  // bread crumb items
  breadCrumbItems: Array<{}>;
  public knowledgebaseForm: FormGroup;
  public isSubmitted: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private router: Router,
    private _knowledgebaseService: KnowledgebaseService) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Knowledgebase' }, { label: 'Create', active: true }];

    this.knowledgebaseForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required],
    })
  }

  createKnowledgebaseItem()
  {
    this.isSubmitted = true;
    if (this.knowledgebaseForm.invalid) {
      return;
    }
    this._knowledgebaseService.createKnowledgebaseItem(this.knowledgebaseForm.value).subscribe()
    this.router.navigate(['/knowledgebase/read'])
  }
}
