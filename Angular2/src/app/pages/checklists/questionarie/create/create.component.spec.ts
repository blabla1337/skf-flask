import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateQuestionarieComponent } from './create.component';

describe('CreateQuestionarieComponent', () => {
  let component: CreateQuestionarieComponent;
  let fixture: ComponentFixture<CreateQuestionarieComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateQuestionarieComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateQuestionarieComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
