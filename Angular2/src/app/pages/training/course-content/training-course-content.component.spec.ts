import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingCourseContentComponent } from './training-course-content.component';

describe('TrainingCourseContentComponent', () => {
  let component: TrainingCourseContentComponent;
  let fixture: ComponentFixture<TrainingCourseContentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingCourseContentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingCourseContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
