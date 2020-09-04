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
});
