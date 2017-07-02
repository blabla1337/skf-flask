import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule } from "@angular/forms";
import { OrderBy } from '../pipes/order-by.pipe'
import { HttpModule } from "@angular/http";
import { Observable } from "rxjs/Observable";

import { fakeAsync } from "@angular/core/testing";
import { tick } from "@angular/core/testing";
import { KnowledgebaseComponent } from "./knowledgebase.component";
import { Knowledgebase } from "../models/knowledgebase";
import { StartsWithPipe } from "../pipes/starts-with.pipe";


describe('Checklist component', () => {
  let component: KnowledgebaseComponent;
  let fixture: ComponentFixture<KnowledgebaseComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;
  let knowledgeBase: Knowledgebase[] = [{ id:1, title:"I am a very specific title for testing the assertion", content:"aa"}]

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [KnowledgebaseComponent, OrderBy, StartsWithPipe],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule]
    }).compileComponents();
})

    beforeEach(() => {
      fixture = TestBed.createComponent(KnowledgebaseComponent)
      component = fixture.componentInstance;
      component.knowledgeitems = knowledgeBase;
      debugElement = fixture.debugElement.query(By.css('section'));
      fixture.detectChanges()
    })

  it('should show quote after getQuote promise (fakeAsync)', fakeAsync(() => {
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('I am a very specific title for testing the assertion');
  }));
})

   