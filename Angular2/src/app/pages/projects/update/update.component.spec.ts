import { async, ComponentFixture, TestBed, tick, fakeAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

import { ProjectUpdateComponent } from './update.component';
import { ProjectManageComponent } from '../manage/manage.component';

describe('ProjectUpdateComponent', () =>
{
  let component: ProjectUpdateComponent;
  let fixture: ComponentFixture<ProjectUpdateComponent>;
  let router: Router;
  let location: Location;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule,
                RouterTestingModule.withRoutes([
                  { path: 'projects/manage', component: ProjectManageComponent },
                ])],
      declarations: [ProjectUpdateComponent]
    })
      .compileComponents();
    router = TestBed.inject(Router);
    location = TestBed.inject(Location);
    router.initialNavigation();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(ProjectUpdateComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should return true', () =>
  {
    component.validSubmit();
    expect(component.submit).toBeTruthy();
  });

  it('should update project item', fakeAsync(() =>
  {
    component.updateProjectItem();
    expect(component.submit).toBeTruthy();
    expect(component.projectForm.valid).toBeFalsy();

    router.navigate(['projects/manage']);
    tick();
    expect(location.path()).toBe('/projects/manage');
  }));
});
