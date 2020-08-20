import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpdateCategoryComponent } from './update.component';

describe('UpdateCategoryComponent', () => {
  let component: UpdateCategoryComponent;
  let fixture: ComponentFixture<UpdateCategoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpdateCategoryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpdateCategoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
