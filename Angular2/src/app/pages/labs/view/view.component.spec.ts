import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';

import { LabViewComponent } from './view.component';
import { LabelFilterPipe } from '../../../core/pipes/labelfilter.pipe'
import { StringFilterPipe } from '../../../core/pipes/stringfilter.pipe'

describe('LabViewComponent', () =>
{
  let component: LabViewComponent;
  let fixture: ComponentFixture<LabViewComponent>;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, RouterTestingModule],
      declarations: [LabViewComponent, LabelFilterPipe, StringFilterPipe],
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(LabViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });
});
