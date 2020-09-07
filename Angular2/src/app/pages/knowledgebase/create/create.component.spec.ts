import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { CreateComponent } from './create.component';

describe('CreateComponent', () =>
{
  let component: CreateComponent;
  let fixture: ComponentFixture<CreateComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [CreateComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(CreateComponent);
    component = fixture.componentInstance;
    component.ngOnInit()
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should valid submit', () =>
  {
    component.validSubmit();
    expect(component.submit).toBeTruthy();
  });

  it('should create knowledgebase item', () =>
  {
    component.createKnowledgebaseItem();
    expect(component.submit).toBeTruthy();
    expect(component.knowledgebaseForm.valid).toBeFalsy();
  });
});
