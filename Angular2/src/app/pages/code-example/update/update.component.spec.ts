import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateCodeComponent } from './update.component';

describe('UpdateCodeComponent', () => {
  let component: UpdateCodeComponent;
  let fixture: ComponentFixture<UpdateCodeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateCodeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateCodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
