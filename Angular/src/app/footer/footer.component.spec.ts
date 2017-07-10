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
import { FooterComponent } from "./footer.component";



describe('Footer component', () => {
  let component: FooterComponent;
  let fixture: ComponentFixture<FooterComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;


  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [FooterComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule]
    }).compileComponents();
  })

  beforeEach(() => {
    fixture = TestBed.createComponent(FooterComponent)
    component = fixture.componentInstance;
    fixture.detectChanges()
  })


  it('check if footer is returned true when if path not taken', () => {
    component.ngOnInit();
    //expect(component.isLoggedin).toBeFalsy()
  });

  it('check if footer is returned false when if path is taken', () => {
    sessionStorage.setItem("auth_token","unit test");
    component.ngOnInit();
    fixture.detectChanges();
    //expect(component.isLoggedin).toBeTruthy()
    sessionStorage.removeItem("auth_token")
  });

})

