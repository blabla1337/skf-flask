import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CodeCreateComponent } from './create.component';

describe('CodeCreateComponent', () => {
  let component: CodeCreateComponent;
  let fixture: ComponentFixture<CodeCreateComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CodeCreateComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CodeCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
