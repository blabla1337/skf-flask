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
import { KnowledgebaseService } from "../services/knowledgebase.service";


describe('Knowledgebase component component', () => {
  let component: KnowledgebaseComponent;
  let fixture: ComponentFixture<KnowledgebaseComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;
  let knowledgeBase: Knowledgebase[] = [{ id: 1, title: "I am a very specific title for testing the assertion", content: "aa" }]
  let test: Knowledgebase[];
  let mockService = Observable.of(knowledgeBase);

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [KnowledgebaseComponent, OrderBy, StartsWithPipe],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule],
      providers: [{ provide: KnowledgebaseService, useClass: mockService }]
    }).compileComponents();
  })

  beforeEach(() => {
    fixture = TestBed.createComponent(KnowledgebaseComponent)
    component = fixture.componentInstance;
    debugElement = fixture.debugElement.query(By.css('section'));
    fixture.detectChanges()
  })

  it('Knowledgebase items should be reflected in the html', fakeAsync(() => {
    component.knowledgeitems = knowledgeBase;
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('I am a very specific title for testing the assertion');
  }));

  it('check if component compiles succesfully', () => {
    component.error = "I am a mocked error";
    fixture.detectChanges();
    expect(debugElement.nativeElement.textContent).toMatch('I am a mocked error');
  });

  it('check if component compiles succesfully', () => {
    expect(component).toBeTruthy();
  });
})

