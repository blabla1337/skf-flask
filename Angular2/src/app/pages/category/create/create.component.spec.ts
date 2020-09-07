import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { CreateCategoryComponent } from './create.component';

describe('CreateCategoryComponent', () =>
{
  let component: CreateCategoryComponent;
  let fixture: ComponentFixture<CreateCategoryComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [CreateCategoryComponent]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(CreateCategoryComponent);
    component = fixture.componentInstance;
    component.ngOnInit()
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should create category', () =>
  {
    component.createCategory();
    expect(component.submit).toBeTruthy();
    expect(component.validationform.valid).toBeFalsy();
  });

  it('should submit valid', () =>
  {
    component.validSubmit();
    expect(component.submit).toBeTruthy();
  });
});
