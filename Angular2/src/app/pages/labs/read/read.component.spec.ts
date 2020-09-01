import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LabReadComponent } from './read.component';

describe('LabReadComponent', () => {
  let component: LabReadComponent;
  let fixture: ComponentFixture<LabReadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LabReadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LabReadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
