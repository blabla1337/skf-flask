import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ChecklistComponent } from './checklist.component';
import { RouterTestingModule } from '@angular/router/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { OrderBy } from '../pipes/order-by.pipe'
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

describe('ChecklistComponent', () => {
  let component: ChecklistComponent;
  let fixture: ComponentFixture<ChecklistComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ChecklistComponent, OrderBy],
      imports: [RouterTestingModule, HttpModule, FormsModule, NgbModule.forRoot()],
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChecklistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the checklist component', () => {
    expect(component).toBeTruthy();
  });
});
