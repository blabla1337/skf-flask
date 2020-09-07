import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { UpdateChecklistTypeComponent } from './update.component';

describe('UpdateChecklistTypeComponent', () =>
{
  let component: UpdateChecklistTypeComponent;
  let fixture: ComponentFixture<UpdateChecklistTypeComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [UpdateChecklistTypeComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(UpdateChecklistTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should valid submit', () =>
  {
    component.validSubmit();
    expect(component.submit).toBeTruthy();
  });

  it('should update checklist item', () =>
  {
    component.updateChecklistItem();
    expect(component.submit).toBeTruthy();
    expect(component.checklistForm.valid).toBeFalsy();
  });
});
