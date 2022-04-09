import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingCourseTreeComponent } from './training-course-tree.component';

describe('TrainingCourseTreeComponent', () => {
  let component: TrainingCourseTreeComponent;
  let fixture: ComponentFixture<TrainingCourseTreeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingCourseTreeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingCourseTreeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
