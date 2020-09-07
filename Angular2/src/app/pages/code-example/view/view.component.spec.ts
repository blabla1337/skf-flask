import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { NgbNavModule } from "@ng-bootstrap/ng-bootstrap";

import { ViewCodeComponent } from './view.component';

describe('ViewCodeComponent', () =>
{
  let component: ViewCodeComponent;
  let fixture: ComponentFixture<ViewCodeComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, NgbNavModule],
      declarations: [ViewCodeComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(ViewCodeComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should show code', () =>
  {
    component.showCode(1);
  });

  it('should login user', () =>
  {
    component.loggedIn();
    expect(component.loggedin).toBeTruthy();
  });

  it('should set category selector id', () =>
  {
    component.setCategorySelectorId(1);
    expect(component).toBeTruthy();
  });
});
