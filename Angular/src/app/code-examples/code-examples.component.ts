import { Component, OnInit, ElementRef } from '@angular/core';
import { CodeExamplesService } from '../services/code-examples.service'
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CodeExample } from '../models/code-example'
import { HighlightJsService } from 'angular2-highlight-js'; // in live this would be the node_modules path
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { CategoryService } from '../services/category.service';
import { Category } from '../models/category';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

declare var hljs: any;

@Component({
  selector: 'app-code-examples',
  templateUrl: './code-examples.component.html',
  providers: [CodeExamplesService, CategoryService, HighlightJsService]
})

export class CodeExamplesComponent implements OnInit
{

  public lang: string;
  public codeExamples: CodeExample[] = [];
  public hljs;
  public queryString;
  public codeLangs;
  codeForm: FormGroup;
  public isSubmitted: boolean;
  public delete: string;
  public category_id: number;
  public categories: Category[];
  public canManage: boolean;
  public selectUndefinedOptionValue: undefined = undefined;

  constructor(private codeService: CodeExamplesService, private categoryService: CategoryService, private highlightJsService: HighlightJsService, private el: ElementRef, private modalService: NgbModal, private formBuilder: FormBuilder)
  {
    this.lang = localStorage.getItem('code_lang')
  }

  get formControls() { return this.codeForm.controls; }

  ngOnInit()
  {

    if (AppSettings.AUTH_TOKEN) {
      const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canManage = decodedJWT.privilege.includes('manage');
    }

    this.codeForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required],
      code_lang: ['', Validators.required]
    })
    this.categoryList();
  }

  storeCodeExample(category_id: number)
  {
    this.isSubmitted = true;
    if (this.codeForm.invalid) {
      return;
    }
    this.codeService.newCodeExample(this.category_id, this.codeForm.value)
      .subscribe(
        () => this.getCodeExamples(this.category_id)
      );
  }

  getCodeExamples(category_id: number)
  {
    this.codeService.getCode(this.category_id)
      .subscribe(examples =>
      {
        this.codeExamples = examples;
        let codeLangSet = new Set();
        this.codeExamples.map(item => codeLangSet.add(item["code_lang"]));
        this.codeLangs = Array.from(codeLangSet);
      },
        () => console.log('There was an error catching code examples.'))
  }

  deleter(id: number)
  {
    if (this.delete == 'DELETE') {
      this.codeService.deleteCodeExample(id).subscribe(x =>
        // Get the new project list on delete
        this.getCodeExamples(this.category_id))
    }
  }

  categoryList()
  {
    this.categoryService
      .getCategories()
      .subscribe(
        categories =>
        {
          this.categories = categories;
          if (this.categories) {
            console.log('There are no projects to show!')
          }
        },
        err => console.log('Getting the projects failed, contact an administrator! '));
  }

  selectChecklistsFromCategory()
  {
    localStorage.setItem("category_id", this.category_id.toString());
    this.getCodeExamples(this.category_id);
  }


  addCodeModal(content)
  {
    this.modalService.open(content, { size: 'lg' }).result
  }

  deleteCodeModal(content)
  {
    this.modalService.open(content, { size: 'lg' }).result
  }

  highlight()
  {
    this.highlightJsService.highlight(this.el.nativeElement.querySelector('#changeme'));
  }
}