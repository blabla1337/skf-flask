import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { NgbNavModule } from "@ng-bootstrap/ng-bootstrap";

import { CheckManageComponent } from './manage.component';

describe('CheckManageComponent', () =>
{
  let component: CheckManageComponent;
  let fixture: ComponentFixture<CheckManageComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule, NgbNavModule],
      declarations: [CheckManageComponent],
      providers: [NgbNavModule]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(CheckManageComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should delete question', () =>
  {
    component.deleteQuestion(1);
  });

  it('should delete requirement', () =>
  {
    component.deleteRequirement(1);
  });
});
