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
  let user: User[] = [{ access: "True", activated: "True", email: "example@owasp.org", userID: 1, userName: "admin" }]
  let mockService = Observable.of(user);
  let userRevoke: User[] = [{ access: "False", activated: "False", email: "example@owasp.org", userID: 1, userName: "admin" }]
  let mockService2 = Observable.of(userRevoke);

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [UserManageComponent, OrderBy, StartsWithPipe],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
      providers: [{ provide: UserService, useClass: mockService }]
    }).compileComponents();
  })

  beforeEach(() => {
    fixture = TestBed.createComponent(UserManageComponent)
    component = fixture.componentInstance;
    debugElement = fixture.debugElement.query(By.css('section'));
    fixture.detectChanges()
  })

  it('Users should be reflected in the template', () => {
    component.users = user;
    component.userList();
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('example@owasp.org');
  });

  it('If user is grant, status of True must be reflected in the template', () => {
    component.users = user;
    component.grant_str = "GRANT";
    component.grant(1);
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('True');
  });

  it('If user is revoke, status of False must be reflected in the template', () => {
    component.users = userRevoke;
    component.revoke_str = "REVOKE";
    component.revoke(1);
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('False');
  });

  it('If the list of users is empty, show error message', fakeAsync(() => {
    component.users = [];
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('There are no users available to show yet!');
  }));

  it('If the list of users is empty, show error message', fakeAsync(() => {
    component.open("foobar")
    fixture.detectChanges(); // update view with quote
  }));
  
  it('check if component compiles succesfully', () => {
    expect(component).toBeTruthy();
  });
})

