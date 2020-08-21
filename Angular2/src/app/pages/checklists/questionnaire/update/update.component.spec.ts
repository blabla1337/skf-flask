import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateQuestionnaireComponent } from './update.component';

describe('UpdateQuestionarieComponent', () =>
{
  let component: UpdateQuestionnaireComponent;
  let fixture: ComponentFixture<UpdateQuestionnaireComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      declarations: [UpdateQuestionnaireComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(UpdateQuestionnaireComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });
});
