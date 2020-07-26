import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { CodeExamplesService } from '../../../core/services/code-examples.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class CreateCodeComponent implements OnInit
{
  id: number;
  private sub: any;
  breadCrumbItems: Array<{}>;
  public codeExampleForm: FormGroup;
  public codeExampleItem: any;
  public isSubmitted: boolean;

  get formControls() { return this.codeExampleForm.controls; }

  constructor(
    private formBuilder: FormBuilder,
    private route: ActivatedRoute,
    private _codeExamplesService: CodeExamplesService,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Code Examples' }, { label: 'Create', active: true }];
    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this.codeExampleForm = this.formBuilder.group({
      title: ['', Validators.required],
      lang: ['', Validators.required],
      content: ['', Validators.required],
    })

    this.codeExampleItem = this._codeExamplesService
      .getCodeExample(this.id)
      .subscribe(item => this.codeExampleForm.patchValue(item))
  }

  createCodeExampleItem()
  {
    this.isSubmitted = true;
    if (this.codeExampleForm.invalid) {
      return;
    }
    this._codeExamplesService.createCodeExample(this.codeExampleForm.value).subscribe()
    this.router.navigate(['/code-example/view'])
  }
}

