import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateChecklistTypeComponent } from './update.component';

describe('UpdateChecklistTypeComponent', () => {
  let component: UpdateChecklistTypeComponent;
  let fixture: ComponentFixture<UpdateChecklistTypeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateChecklistTypeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateChecklistTypeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
