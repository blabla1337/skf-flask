import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TrainingContentMarkdownComponent } from './training-content-markdown.component';

describe('TrainingContentMarkdownComponent', () => {
  let component: TrainingContentMarkdownComponent;
  let fixture: ComponentFixture<TrainingContentMarkdownComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TrainingContentMarkdownComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TrainingContentMarkdownComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
