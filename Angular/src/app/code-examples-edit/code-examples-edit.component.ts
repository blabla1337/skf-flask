import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { CodeExamplesService } from '../services/code-examples.service'

import { QuestionsService } from '../services/questions.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';
import { CodeExample } from '../models/code-example';
import { Observable } from 'rxjs';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { tap } from 'rxjs/operators';



@Component({
  selector: 'app-code-examples-edit',
  templateUrl: './code-examples-edit.html',
  providers: [ChecklistService, QuestionsService, CodeExamplesService]
})
export class CodeExamplesEditComponent implements OnInit
{

  constructor(private codeService: CodeExamplesService, private route: ActivatedRoute, private router: Router, private formBuilder: FormBuilder) { }

  codeForm: FormGroup;
  public title: string;
  public canEdit: string;
  public IdFromUrl: number;
  public isSubmitted: boolean;
  codeItem: Observable<CodeExample>;
  codeItemArray: CodeExample[];

  get formControls() { return this.codeForm.controls; }

  ngOnInit()
  {
    this.codeForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required],
      code_lang: ['', Validators.required],
    })

    this.route.params.subscribe(params =>
    {
      this.IdFromUrl = params['id'];
    });

    this.codeItem = this.codeService.getCodeExample(this.IdFromUrl).pipe(
      tap(codeItem => this.codeForm.patchValue(codeItem))
    );
  }

  updateCodeItem()
  {
    this.isSubmitted = true;
    if (this.codeForm.invalid) {
      return;
    }
    this.codeService.updateCodeExample(Number(this.IdFromUrl), this.codeForm.value)
      .subscribe(
        () => console.log('updating code example'),
        () => console.log('Error updating code example')
      );
    let category_id = localStorage.getItem("category_id")
    this.codeService.getCode(Number(category_id)).subscribe(examples => { this.codeItemArray = examples }, () => console.log('There was an error catching code examples.'))
    this.router.navigate(['/code-examples']);
  }

  back()
  {
    this.router.navigate(['/code-examples']);
  }
}