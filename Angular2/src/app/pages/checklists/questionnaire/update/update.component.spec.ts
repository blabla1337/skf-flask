import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { UpdateQuestionnaireComponent } from './update.component';

describe('UpdateQuestionarieComponent', () =>
{
  let component: UpdateQuestionnaireComponent;
  let fixture: ComponentFixture<UpdateQuestionnaireComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [UpdateQuestionnaireComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(UpdateQuestionnaireComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
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

  it('should update question item', () =>
  {
    component.updateQuestionItem();
    expect(component.submit).toBeTruthy();
    expect(component.questionForm.valid).toBeFalsy();
  });
});
