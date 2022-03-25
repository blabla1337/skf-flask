import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingContentEmptyComponent } from './training-content-empty.component';

describe('TrainingContentEmptyComponent', () => {
  let component: TrainingContentEmptyComponent;
  let fixture: ComponentFixture<TrainingContentEmptyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingContentEmptyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingContentEmptyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
