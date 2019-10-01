import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
import { OrderBy } from '../pipes/order-by.pipe'
import { HttpModule } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { fakeAsync } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { StartsWithPipe } from '../pipes/starts-with.pipe';
import { FirstLoginComponent } from './first-login.component';


describe('First login component', () => {
  let component: FirstLoginComponent;
  let fixture: ComponentFixture<FirstLoginComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;


  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [FirstLoginComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule]
    }).compileComponents();
})

    beforeEach(() => {
      fixture = TestBed.createComponent(FirstLoginComponent)
      component = fixture.componentInstance;
      fixture.detectChanges()
    })


    it('check if errors are all triggered on empty input fields', () => {
    component.activateUser();
    fixture.detectChanges();
    expect(component.error).toMatch('AccessToken');
    expect(component.error).toMatch('Email');
    expect(component.error).toMatch('Password');
    expect(component.error).toMatch('Repassword');
    expect(component.error).toMatch('UserID');
    expect(component.error).toMatch('Username');
    expect(component.return).toBeFalsy()

  });

    it('check if component compiles succesfully', () => {
    expect(component).toBeTruthy();
  });
})


