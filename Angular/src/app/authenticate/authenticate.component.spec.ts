import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AuthenticateComponent } from './authenticate.component';

describe('LoginComponent', () => {
  let component: AuthenticateComponent;
  let fixture: ComponentFixture<AuthenticateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AuthenticateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuthenticateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
