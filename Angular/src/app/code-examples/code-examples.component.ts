import { Component, OnInit, ElementRef } from '@angular/core';
import { CodeExamplesService } from '../services/code-examples.service'
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { CodeExample } from '../models/code-example'
import { HighlightJsService } from 'angular2-highlight-js'; // in live this would be the node_modules path
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';

declare var hljs: any;

@Component({
  selector: 'app-code-examples',
  templateUrl: './code-examples.component.html',
  providers: [CodeExamplesService, HighlightJsService]
})

export class CodeExamplesComponent implements OnInit {

  public lang: string;
  public codeExamples: CodeExample[] = [];
  public hljs;
  public queryString;
  codeForm: FormGroup;
  public isSubmitted: boolean;
  public delete: string;
  
  constructor(private codeService: CodeExamplesService, private highlightJsService: HighlightJsService, private el: ElementRef, private modalService: NgbModal, private formBuilder: FormBuilder) {
    this.lang = localStorage.getItem('code_lang')
  }

  get formControls() { return this.codeForm.controls; }

  ngOnInit() {
    this.codeForm = this.formBuilder.group({
      title: ['', Validators.required],
      content: ['', Validators.required],
      code_lang: ['', Validators.required]
    })
    this.getCodeExamples();
  }

  storeCodeExample() {
    this.isSubmitted = true;
    if(this.codeForm.invalid){
      return;
    }
    this.codeService.newCodeExample(this.codeForm.value)
      .subscribe(
      () => this.getCodeExamples()
      );
    () => console.log('Eror storing a new knowledgebase item!')
  }

  getCodeExamples() {
    this.codeService.getCode()
      .subscribe(examples => {
        this.codeExamples = examples
      },
        err => console.log('There was an error catching code examples.'))
  }

  deleter(id: number) {
    if (this.delete == 'DELETE') {
      this.codeService.deleteCodeExample(id).subscribe(x =>
        // Get the new project list on delete
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
