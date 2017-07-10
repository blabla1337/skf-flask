import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UndefinedComponent } from './undefined.component';

describe('UndefinedComponent', () => {
  let component: UndefinedComponent;
  let fixture: ComponentFixture<UndefinedComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UndefinedComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UndefinedComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should be created', () => {
    expect(component).toBeTruthy();
  });
});
