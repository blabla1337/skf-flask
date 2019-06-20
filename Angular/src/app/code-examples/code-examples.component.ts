import { Component, OnInit, DoCheck, ElementRef } from '@angular/core';
import { CodeExamplesService } from '../services/code-examples.service'
import { AppSettings } from '../globals';
import { CodeExample } from '../models/code-example'
import { HighlightJsService } from 'angular2-highlight-js'; //in live this would be the node_modules path
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

declare var hljs: any;

@Component({
  selector: 'app-code-examples',
  templateUrl: './code-examples.component.html',
  providers: [CodeExamplesService, HighlightJsService]
})

export class CodeExamplesComponent implements OnInit, DoCheck {

  public lang: string;
  public codeExamples: CodeExample[] = [];
  public error: string;
  public hljs;
  public queryString;
  public title:string;
  public content: string;
  public code_lang: string;
  public return: boolean;
  public errors: string[]
  public delete: string;
  public postHeaders = new Headers({ 'Content-Type': 'application/json', 'Authorization': AppSettings.AUTH_TOKEN });

  constructor(private codeService: CodeExamplesService, private highlightJsService: HighlightJsService, private el: ElementRef, private modalService: NgbModal) {
    this.lang = localStorage.getItem("code_lang")
  }

  ngOnInit() {
    this.getCodeExamples();
  }

  storeCodeExample() {

    this.errors = [];
    this.return = true;

    if (!this.title) { this.errors.push("Title was left empty"); this.return = false; }
    if (!this.content) { this.errors.push("Content was left empty"); this.return = false; }
    if (!this.code_lang) { this.errors.push("Content was left empty"); this.return = false; }
    if (this.return == false) { return; }

    this.errors = [];
    this.codeService.newCodeExample(this.title, this.content, this.code_lang)
      .subscribe(
        () => this.errors.push("Eror storing a new knowledgebase item!")
      );
    this.getCodeExamples();
  }

  getCodeExamples() {
    this.codeService.getCode()
      .subscribe(examples => {
        this.codeExamples = examples
      },
        err => this.error = "There was an error catching code examples.")
  }

  deleter(id: number) {
    if (this.delete == "DELETE") {
      this.codeService.deleteCodeExample(id).subscribe(x =>
        //Get the new project list on delete 
        this.getCodeExamples())
    }
  }

  addCodeModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  deleteCodeModal(content) {
    this.modalService.open(content, { size: 'lg' }).result
  }

  highlight() {
    this.highlightJsService.highlight(this.el.nativeElement.querySelector('#changeme'));
  }
}
