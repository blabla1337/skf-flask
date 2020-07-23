import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewKnowledebaseComponent } from './view.component';

describe('ViewKnowledebaseComponent', () => {
  let component: ViewKnowledebaseComponent;
  let fixture: ComponentFixture<ViewKnowledebaseComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ViewKnowledebaseComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ViewKnowledebaseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
