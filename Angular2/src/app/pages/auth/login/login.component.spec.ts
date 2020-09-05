import { async, ComponentFixture, TestBed, tick, fakeAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { Location } from '@angular/common';

import { LoginComponent } from './login.component';
import { HomeComponent } from '../../dashboard/home/home.component';
import { RegisterComponent } from '../register/register.component';

import { AuthService } from '../../../core/services/auth.service';
import { Token } from '@angular/compiler/src/ml_parser/lexer';
import { Router } from '@angular/router';
import { PagesRoutingModule } from '../../pages-routing.module';

describe('LoginComponent', () =>
{
  let component: LoginComponent;
  let router: Router;
  let location: Location;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [
        HttpClientTestingModule,
        RouterTestingModule.withRoutes([
          { path: 'dashboard', component: HomeComponent },
          { path: 'auth', loadChildren: () => import('../auth.module').then(m => m.AuthModule)},
        ]),
        ReactiveFormsModule, FormsModule],
      declarations: [LoginComponent],
      providers: [Location]
    })
      .compileComponents();

    router = TestBed.inject(Router);
    location = TestBed.inject(Location);
    fixture = TestBed.createComponent(LoginComponent);
    router.initialNavigation();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('form invalid when empty', () => {
    expect(component.loginForm.valid).toBeFalse();
  });

  it('username field validity', () => {
    let username = component.loginForm.controls['username'];
    expect(username.valid).toBeFalsy();

    let errors = {};
    errors = username.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('password field validity', () => {
    let password = component.loginForm.controls['password'];
    expect(password.valid).toBeFalsy();

    let errors = {};
    errors = password.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('navigate to "dashboard" takes us to /dashboard', fakeAsync(() => {
    component.onSkip();
    router.navigate(['dashboard']);
    tick();
    expect(location.path()).toBe('/dashboard');
  }));

  // it('navigate to "register" takes us to /auth/register', fakeAsync(() => {
  //   component.onRegister();
  //   router.navigate(['auth', 'register']);
  //   tick();
  //   expect(location.path()).toBe('/auth/register');
  // }));

});
