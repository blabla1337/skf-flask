import { async, ComponentFixture, TestBed, inject } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { of } from 'rxjs';

import { UpdateChecklistTypeComponent } from './update.component';
import { ChecklistService } from '../../../../core/services/checklists.service'
import { Inject, Component } from '@angular/core';
import { ItemsList } from '@ng-select/ng-select/lib/items-list';

describe('UpdateChecklistTypeComponent', () =>
{
  let component: UpdateChecklistTypeComponent;
  let fixture: ComponentFixture<UpdateChecklistTypeComponent>;
  let checklistService;
  let element;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [UpdateChecklistTypeComponent],
      providers: [ChecklistService]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(UpdateChecklistTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  beforeEach(inject([ChecklistService], s => {
    checklistService = s;
    fixture = TestBed.createComponent(UpdateChecklistTypeComponent);
    component = fixture.componentInstance;
    element = fixture.nativeElement;
  }));

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
