import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateQuestionarieComponent } from './update.component';

describe('UpdateQuestionarieComponent', () => {
  let component: UpdateQuestionarieComponent;
  let fixture: ComponentFixture<UpdateQuestionarieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateQuestionarieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateQuestionarieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
