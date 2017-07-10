import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule } from "@angular/forms";
import { OrderBy } from '../pipes/order-by.pipe'
import { HttpModule } from "@angular/http";
import { Observable } from "rxjs/Observable";
import { fakeAsync } from "@angular/core/testing";
import { RouterTestingModule } from '@angular/router/testing';

import { StartsWithPipe } from "../pipes/starts-with.pipe";
import { CodeExamplesComponent } from "./code-examples.component";
import { CodeExample } from "../models/code-example";
import { HighlightJsService } from "angular2-highlight-js/lib/highlight-js.service";


describe('Code examples component', () => {
  let component: CodeExamplesComponent;
  let fixture: ComponentFixture<CodeExamplesComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;
  let stub: CodeExample[] = [{ codeID:1, content_lang: "PHP", title:"File upload",content:"File upload injections content"}]
  
  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [CodeExamplesComponent, OrderBy, StartsWithPipe],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
    }).compileComponents();
})

    beforeEach(() => {
      fixture = TestBed.createComponent(CodeExamplesComponent)
      component = fixture.componentInstance;
      component.codeExamples = stub;
      debugElement = fixture.debugElement.query(By.css('section'));
      fixture.detectChanges()
    })

  it('Code example item should be reflected in the html', fakeAsync(() => {
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('File upload');
  }));

  it('check if component compiles succesfully', () => {
    expect(component).toBeTruthy();
  });
})

   