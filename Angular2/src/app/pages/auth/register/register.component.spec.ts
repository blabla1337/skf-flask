import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule, FormsModule, Validators, FormBuilder } from '@angular/forms';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { RegisterComponent } from './register.component';

describe('RegisterComponent', () =>
{
  let component: RegisterComponent;
  let fixture: ComponentFixture<RegisterComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [RegisterComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(RegisterComponent);
    component = fixture.componentInstance;
    component.ngOnInit()
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('form invalid when empty', () => {
    expect(component.registerationForm.valid).toBeFalse();
  });

  it('form should be valid', () => {
    component.registerationForm.controls.username.setValue('sasd');
    component.registerationForm.controls.email.setValue('sadasd@asd.com');
    component.registerationForm.controls.user_id.setValue('132456789');
    component.registerationForm.controls.password.setValue('qwerty@123');
    component.registerationForm.controls.repassword.setValue('qwerty@123');
    component.registerationForm.controls.accessToken.setValue('12345');
    expect(component.registerationForm.valid).toBeTruthy();
  });

  it('username field validity', () => {
    let username = component.registerationForm.controls['username'];
    expect(username.valid).toBeFalsy();

    let errors = {};
    errors = username.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('email field validity', () => {
    let email = component.registerationForm.controls['email'];
    expect(email.valid).toBeFalsy();

    let errors = {};
    errors = email.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('password field validity', () => {
    let password = component.registerationForm.controls['password'];
    expect(password.valid).toBeFalsy();

    let errors = {};
    errors = password.errors || {};
    expect(errors['required']).toBeTruthy();

    password.setValue('1234567');
    errors = password.errors || {};
    expect(errors['minlength']).toBeDefined();
  });

  it('userid field validity', () => {
    let user_id = component.registerationForm.controls['user_id'];
    expect(user_id.valid).toBeFalsy();

    let errors = {};
    errors = user_id.errors || {};
    expect(errors['required']).toBeTruthy();

    user_id.setValue('1a-/');
    errors = user_id.errors || {};
    expect(errors['pattern']).toBeTruthy();
  });

  it('access token field validity', () => {
    let accessToken = component.registerationForm.controls['accessToken'];
    expect(accessToken.valid).toBeFalsy();

    let errors = {};
    errors = accessToken.errors || {};
    expect(errors['required']).toBeTruthy();

    accessToken.setValue('1a-/');
    errors = accessToken.errors || {};
    expect(errors['pattern']).toBeTruthy();
  });

  it('should be reset', () =>
  {
    component.onReset();
    expect(component.userSubmitted).toBeFalsy();
    expect(component.registerationForm.reset).toBeTruthy();
  });

});
