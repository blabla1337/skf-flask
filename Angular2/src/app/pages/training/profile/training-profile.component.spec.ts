import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingProfileComponent } from './training-profile.component';

describe('TrainingProfileComponent', () => {
  let component: TrainingProfileComponent;
  let fixture: ComponentFixture<TrainingProfileComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingProfileComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
