import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateChecklistTypeComponent } from './create.component';

describe('CreateChecklistTypeComponent', () => {
  let component: CreateChecklistTypeComponent;
  let fixture: ComponentFixture<CreateChecklistTypeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateChecklistTypeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateChecklistTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
