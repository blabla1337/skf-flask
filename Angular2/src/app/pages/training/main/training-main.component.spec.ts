import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingMainComponent } from './training-main.component';

describe('CourseMainComponent', () => {
  let component: TrainingMainComponent;
  let fixture: ComponentFixture<TrainingMainComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingMainComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingMainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
