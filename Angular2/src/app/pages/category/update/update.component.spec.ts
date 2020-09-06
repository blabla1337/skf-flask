import { async, ComponentFixture, TestBed, tick, fakeAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

import { UpdateCategoryComponent } from './update.component';
import { CategoryManageComponent } from '../manage/manage.component';

describe('UpdateCategoryComponent', () =>
{
  let component: UpdateCategoryComponent;
  let fixture: ComponentFixture<UpdateCategoryComponent>;
  let router: Router;
  let location: Location;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, 
                RouterTestingModule.withRoutes([
                  { path: 'category/manage', component: CategoryManageComponent },
                ])],
      declarations: [UpdateCategoryComponent]
    })
      .compileComponents();
    router = TestBed.inject(Router);
    location = TestBed.inject(Location);
    router.initialNavigation();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(UpdateCategoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should create valid form', () =>
  {
    component.validSubmit();
    expect(component.submit).toBeTruthy();
  });

  it('should upate category', fakeAsync(() =>
  {
    component.updateCategory();
    expect(component.submit).toBeTruthy();
    expect(component.validationform.valid).toBeFalsy();

    router.navigate(['category/manage']);
    tick();
    expect(location.path()).toBe('/category/manage');
  }));
});
