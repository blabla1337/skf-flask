import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { WizardComponent } from './wizard.component';

describe('WizardComponent', () =>
{
  let component: WizardComponent;
  let fixture: ComponentFixture<WizardComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [WizardComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(WizardComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should assign value', () =>
  {
    component.onChange('12345');
    expect(component.selected).toBe('12345');
  });

  it('form invalid when empty', () => {
    component.storeSprint();
    expect(component.isSubmitted).toBeTrue();
    expect(component.newSprintForm.valid).toBeFalsy();
  });
});
