import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OpenidComponent } from './openid.component';

describe('OpenidComponent', () => {
  let component: OpenidComponent;
  let fixture: ComponentFixture<OpenidComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OpenidComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OpenidComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
