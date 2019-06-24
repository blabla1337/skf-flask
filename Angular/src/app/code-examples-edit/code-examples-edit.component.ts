import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { ChecklistService } from '../services/checklist.service'
import { CodeExamplesService } from '../services/code-examples.service'

import { QuestionsService } from '../services/questions.service'
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';



@Component({
  selector: 'app-code-examples-edit',
  templateUrl: './code-examples-edit.html',
  providers: [ChecklistService, QuestionsService, CodeExamplesService]
})
export class CodeExamplesEditComponent implements OnInit {

  constructor(
    private _codeService: CodeExamplesService,
    private route: ActivatedRoute,
    private router: Router,
  ) { }

  public canEdit: string;
  public knowledgebaseID: number;
  public return: boolean;
  public errors: string[];
  public error: string;
  public IdFromUrl: number;
  public title: string;
  public content: string;
  public code_lang: string;
  public codeExample: any[];

  ngOnInit() {

    this.route.params.subscribe(params => {
      this.IdFromUrl = params['id'];
    });

    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canEdit = decodedJWT.privilege.includes('edit');
    }
    setTimeout(() => {
      this.getCodeItem();
    }, 500);
  }

  updateCodeItem() {
    this.errors = [];
    this.return = true;

    if (!this.title) { this.errors.push('Title was left empty'); this.return = false; }
    if (!this.content) { this.errors.push('Content was left empty'); this.return = false; }
    if (!this.code_lang) { this.errors.push('code language was left empty'); this.return = false; }
    if (this.return == false) { return; }

    this.errors = [];
    this._codeService.updateCodeExample(Number(this.IdFromUrl), this.title, this.content, this.code_lang)
      .subscribe(
        () => this.back(),
        () => this.errors.push('Error updating code example')
      );

    this._codeService.getCode().subscribe(examples => {this.codeExample = examples},err => this.error = 'There was an error catching code examples.')
    this.router.navigate(['/code-examples']);
  }

  getCodeItem() {
    this._codeService.getCodeExample(this.IdFromUrl).subscribe(
      codeExample => {
        this.content = codeExample['content']
        this.code_lang = codeExample['code_lang']
        this.title = codeExample['title']
      },
      err => this.error = 'Error getting knowledge items, contact the administrator!'
    );
  }

  back() {
    this.router.navigate(['/code-examples']);
  }
}
