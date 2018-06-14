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
import { StartsWithPipe } from "../pipes/starts-with.pipe";
import { UserService } from "../services/user-manage.service";
import { UserManageComponent } from "./user-manage.component";
import { User } from "../models/user";
import { RouterTestingModule } from "@angular/router/testing";
import { ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';

describe('Users manage component', () => {
  let component: UserManageComponent;
  let fixture: ComponentFixture<UserManageComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;
  let user: User[] = [{ access: "True", active: "True", email: "example@owasp.org", userID: 1, accessToken: 1234, userName: "admin" }]
  let userRevoke: User[] = [{ access: "False", active: "False", email: "example@owasp.org", userID: 1, accessToken: 1234, userName: "admin" }]
  let mocker = {
    revoke: jasmine.createSpy('revoke'),
    grant: jasmine.createSpy('grant')
  }

  beforeEach(async () => {


    TestBed.configureTestingModule({
      declarations: [UserManageComponent, OrderBy, StartsWithPipe],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
      providers: [{ provide: UserService, useClass: mocker }]
    }).compileComponents();
  })

  beforeEach(() => {
    fixture = TestBed.createComponent(UserManageComponent)
    component = fixture.componentInstance;
    debugElement = fixture.debugElement.query(By.css('section'));
    mocker.revoke.and.returnValue(Observable.of(user))
    mocker.grant.and.returnValue(Observable.of(user))
    fixture.detectChanges()
  })

  it('Users should be reflected in the template', () => {
    component.users = user;
    component.userList();
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('example@owasp.org');
  });

  it('If user is grant, status of True must be reflected in the template', () => {
    component.grant(1);
    component.grant_str = "GRANT";
    component.users = user;
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('True');
  });

  it('If user is revoke, status of False must be reflected in the template', () => {
    component.revoke(1);
      component.users = userRevoke;
    component.revoke_str = "REVOKE";
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('False');
  });

  it('If the list of users is empty, show error message', fakeAsync(() => {
    component.open("admin")
    fixture.detectChanges(); // update view with quote
  }));
  
  it('check if component compiles succesfully', () => {
    expect(component).toBeTruthy();
  });
})

