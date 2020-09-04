import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { StringFilterPipe } from '../../../core/pipes/stringfilter.pipe'
import { ChecklistsReadComponent } from './read.component';

describe('ChecklistsReadComponent', () =>
{
  let component: ChecklistsReadComponent;
  let fixture: ComponentFixture<ChecklistsReadComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      declarations: [ChecklistsReadComponent, StringFilterPipe],
      providers: [StringFilterPipe]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(ChecklistsReadComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    spyOn(component.router, 'navigate');
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });
});
