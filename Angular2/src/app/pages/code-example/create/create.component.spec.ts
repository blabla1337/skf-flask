import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateCodeComponent } from './create.component';

describe('CreateCodeComponent', () => {
  let component: CreateCodeComponent;
  let fixture: ComponentFixture<CreateCodeComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateCodeComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateCodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
