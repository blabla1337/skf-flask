import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateChecklistComponent } from './updatechecklist.component';

describe('UpdateChecklistComponent', () => {
  let component: UpdateChecklistComponent;
  let fixture: ComponentFixture<UpdateChecklistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateChecklistComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateChecklistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
