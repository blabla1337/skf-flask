import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingContentLabComponent } from './training-content-lab.component';

describe('TrainingContentLabComponent', () => {
  let component: TrainingContentLabComponent;
  let fixture: ComponentFixture<TrainingContentLabComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingContentLabComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingContentLabComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
