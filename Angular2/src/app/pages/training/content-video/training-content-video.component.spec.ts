import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingContentVideoComponent } from './training-content-video.component';

describe('TrainingContentVideoComponent', () => {
  let component: TrainingContentVideoComponent;
  let fixture: ComponentFixture<TrainingContentVideoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingContentVideoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingContentVideoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
