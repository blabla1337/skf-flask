import { Component, OnInit, DoCheck, ElementRef } from '@angular/core';
import { CodeExamplesService } from '../services/code-examples.service'
import { StartsWithPipe } from '../pipes/starts-with.pipe'
import { CodeExample } from '../models/code-example'
import { HighlightJsService } from 'angular2-highlight-js'; //in live this would be the node_modules path
import { Observable } from 'rxjs/Rx';

declare var hljs: any;

@Component({
  selector: 'app-code-examples',
  templateUrl: './code-examples.component.html',
  providers: [CodeExamplesService, HighlightJsService]
})

export class CodeExamplesComponent implements OnInit, DoCheck {

  lang: string;
  codeExamples: CodeExample[];
  public error: string;

  constructor(private code: CodeExamplesService, private highlightJsService: HighlightJsService, private el: ElementRef) {
    this.lang = localStorage.getItem("code_lang")
  }

  ngOnInit() {
    this.code.getCode(localStorage.getItem("code_lang"))
      .subscribe(examples => {
        this.codeExamples = examples
        if (!this.codeExamples) {
          this.error = "There was an error getting the code examples!"
        }
      },
      err => this.error = "There was an error catching code examples.")
  }

  ngDoCheck() {
    if (this.lang != localStorage.getItem("code_lang")) {
      this.lang = localStorage.getItem("code_lang")
      this.code.getCode(localStorage.getItem("code_lang"))
        .subscribe(examples => {
          this.codeExamples = examples
          if (!this.codeExamples) {
            this.error = "There was an error getting the code examples!"
          }
        },
        err => this.error = "There was an error catching code examples.")
    }
    this.lang = localStorage.getItem("code_lang")
  }

  highlight() {
    this.highlightJsService.highlight(this.el.nativeElement.querySelector('#changeme'));
  }
}