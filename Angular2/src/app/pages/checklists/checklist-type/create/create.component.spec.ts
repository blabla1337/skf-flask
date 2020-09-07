import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { CreateChecklistTypeComponent } from './create.component';

describe('CreateChecklistTypeComponent', () =>
{
  let component: CreateChecklistTypeComponent;
  let fixture: ComponentFixture<CreateChecklistTypeComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [CreateChecklistTypeComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(CreateChecklistTypeComponent);
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

  it('name field validity', () => {
    let name = component.checklistForm.controls['name'];
    expect(name.valid).toBeFalsy();

    let errors = {};
    errors = name.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('description field validity', () => {
    let description = component.checklistForm.controls['description'];
    expect(description.valid).toBeFalsy();

    let errors = {};
    errors = description.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('visibility field validity', () => {
    let visibility = component.checklistForm.controls['visibility'];
    expect(visibility.valid).toBeFalsy();

    let errors = {};
    errors = visibility.errors || {};
    expect(errors['required']).toBeTruthy();
  });

  it('form invalid when empty', () => {
    component.createChecklistType();
    expect(component.checklistForm.invalid).toBeTruthy();
  });
});
