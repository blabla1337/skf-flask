import { async, ComponentFixture, TestBed, tick, fakeAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

import { CategoryManageComponent } from './manage.component';
import { ProjectManageComponent } from '../../projects/manage/manage.component';

describe('CategoryManageComponent', () =>
{
  let component: CategoryManageComponent;
  let fixture: ComponentFixture<CategoryManageComponent>;
  let router: Router;
  let location: Location;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule,
                RouterTestingModule.withRoutes([
                  { path: 'projects/manage', component: ProjectManageComponent },
                ])],
      declarations: [CategoryManageComponent]
    })
      .compileComponents();
    router = TestBed.inject(Router);
    location = TestBed.inject(Location);
    router.initialNavigation();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(CategoryManageComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('navigate to "manage" takes us to projects/manage', fakeAsync(() => {
    component.onSubmit();
    router.navigate(['projects/manage']);
    tick();
    expect(location.path()).toBe('/projects/manage');
  }));
});
