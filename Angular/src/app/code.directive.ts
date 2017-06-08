import { Component, OnInit, DoCheck, ElementRef, AfterViewInit, Directive } from '@angular/core';
declare var hljs: any;

@Directive({
  selector: 'code[highlight]'
})
export class HighlightCodeDirective {
  constructor(private eltRef:ElementRef) {
  }

  ngAfterViewInit() {
    hljs.highlightBlock(this.eltRef.nativeElement);
  }
}