import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingCourseButtonsComponent } from './training-course-buttons.component';

describe('TrainingCourseButtonsComponent', () => {
  let component: TrainingCourseButtonsComponent;
  let fixture: ComponentFixture<TrainingCourseButtonsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingCourseButtonsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingCourseButtonsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
