import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckManageComponent } from './manage.component';

describe('CheckManageComponent', () => {
  let component: CheckManageComponent;
  let fixture: ComponentFixture<CheckManageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CheckManageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckManageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
