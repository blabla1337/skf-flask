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
import { HeaderComponent } from "./header.component";




describe('Header component', () => {
  let component: HeaderComponent;
  let fixture: ComponentFixture<HeaderComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;


  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [HeaderComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule]
    }).compileComponents();
  })

  beforeEach(() => {
    fixture = TestBed.createComponent(HeaderComponent)
    component = fixture.componentInstance;
    fixture.detectChanges()
  })


  it('check ProjectsShow to return true', () => {
    component.ProjectsShow();
    expect(component.projects).toBeTruthy()
  });

  it('check UsersShow to return true', () => {
    component.UsersShow();
    expect(component.users).toBeTruthy()
  });

  it('check GroupsShow to return true', () => {
    component.GroupsShow();
    expect(component.groups).toBeTruthy()
  });

  it('check ResultsShow to return true', () => {
    component.ResultsShow();
    expect(component.results).toBeTruthy()
  });

  it('check CodeShow to return true', () => {
    component.CodeShow();
    expect(component.code).toBeTruthy()
  });

  it('check KnowledgeShow to return true', () => {
    component.KnowledgeShow();
    expect(component.knowledge).toBeTruthy()
  });

  it('check CheckShow to return true', () => {
    component.CheckShow();
    expect(component.check).toBeTruthy()
  });

  it('check ResetAll to return true', () => {
    component.ResetAll();
    expect(component.check).toBeFalsy()
    expect(component.check).toBeFalsy()
    expect(component.knowledge).toBeFalsy()
    expect(component.code).toBeFalsy()
    expect(component.results).toBeFalsy()
    expect(component.groups).toBeFalsy()
    expect(component.projects).toBeFalsy()
  });


  it('check getProjectStyle banner color to return true', () => {
    component.projects = true;
    component.getProjectStyle();
    expect(component.color).toEqual('#515594')  
  });

  it('check getChecklistStyle banner color to return true', () => {
    component.check = true;
    component.getChecklistStyle();
    expect(component.color).toEqual('#515594')
  });

  it('check getGroupStyle banner color to return true', () => {
    component.groups = true;
    component.getGroupStyle();
    expect(component.color).toEqual('#515594')
  });


  it('check getCodeStyle banner color to return true', () => {
    component.code = true;
    component.getCodeStyle();
    expect(component.color).toEqual('#515594')
  });


  it('check getKnowledgeStyle banner color to return true', () => {
    component.knowledge = true;
    component.getKnowledgeStyle();
    expect(component.color).toEqual('#515594')
  });


  it('check getChecklistStyle banner color to return true', () => {
    component.check = true;
    component.getChecklistStyle();
    expect(component.color).toEqual('#515594')
  });


  it('check if footer is returned false when if path is taken', () => {
    sessionStorage.setItem("auth_token", "unit test");
    component.ngOnInit();
    fixture.detectChanges();
    //expect(component.isLoggedin).toBeTruthy()
  });

})

