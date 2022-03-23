import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingContentLabLanguageComponent } from './training-content-lab-language.component';

describe('TrainingContentLabLanguageComponent', () => {
  let component: TrainingContentLabLanguageComponent;
  let fixture: ComponentFixture<TrainingContentLabLanguageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingContentLabLanguageComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingContentLabLanguageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
