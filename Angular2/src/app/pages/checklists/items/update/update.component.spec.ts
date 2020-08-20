import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateCheckComponent } from './update.component';

describe('UpdateCheckComponent', () => {
  let component: UpdateCheckComponent;
  let fixture: ComponentFixture<UpdateCheckComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateCheckComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateCheckComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
