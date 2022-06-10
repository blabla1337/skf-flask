import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import {  CodeExamplesService } from '../../../core/services/code-examples.service';

@Component({
  selector: 'app-hard-link',
  templateUrl: './hard-link.component.html',
  styleUrls: ['./hard-link.component.scss']
})
export class HardLinkCodeComponent implements OnInit
{
  public id: number;
  private sub: any;
  public breadCrumbItems: Array<{}>;
  public codeItem: any = [];

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor(
    private route: ActivatedRoute,
    private _codeExampleService: CodeExamplesService,
    private router: Router) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Code examples' }, { label: 'hard-link', active: true }];

    this.sub = this.route.params.subscribe(params =>
    {
      this.id = +params['id'];
    });

    this._codeExampleService
      .getCodeExample(this.id)
      .subscribe(item => this.codeItem = item)
  }
}

