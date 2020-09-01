import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChecklistsReadComponent } from './read.component';

describe('ChecklistsReadComponent', () => {
  let component: ChecklistsReadComponent;
  let fixture: ComponentFixture<ChecklistsReadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChecklistsReadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChecklistsReadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
