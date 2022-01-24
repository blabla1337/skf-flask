import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { StringFilterPipe } from '../../../core/pipes/stringfilter.pipe'
import { ProjectManageComponent } from './manage.component';


describe('ProjectManageComponent', () =>
{
  let component: ProjectManageComponent;
  let fixture: ComponentFixture<ProjectManageComponent>;

  beforeEach(waitForAsync(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
      declarations: [ProjectManageComponent, StringFilterPipe]
    })
      .compileComponents();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(ProjectManageComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });
});
