import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewCodeComponent } from './view.component';

describe('ViewCodeComponent', () => {
  let component: ViewCodeComponent;
  let fixture: ComponentFixture<ViewCodeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewCodeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewCodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
