import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HorizontaltopbarComponent } from './horizontaltopbar.component';

describe('HorizontaltopbarComponent', () => {
  let component: HorizontaltopbarComponent;
  let fixture: ComponentFixture<HorizontaltopbarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HorizontaltopbarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HorizontaltopbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
