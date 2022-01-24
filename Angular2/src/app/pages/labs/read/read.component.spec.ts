import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { LabReadComponent } from './read.component';

describe('LabReadComponent', () => {
  let component: LabReadComponent;
  let fixture: ComponentFixture<LabReadComponent>;

  beforeEach(waitForAsync(() => {
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
