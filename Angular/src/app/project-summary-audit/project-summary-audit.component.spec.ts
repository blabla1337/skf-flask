import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ProjectSummaryAuditComponent } from './project-summary-audit.component';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterTestingModule } from '@angular/router/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

describe('ProjectSummaryComponent', () => {
  let component: ProjectSummaryAuditComponent;
  let fixture: ComponentFixture<ProjectSummaryAuditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProjectSummaryAuditComponent ],
      imports:[NgbModule.forRoot(), FormsModule, RouterTestingModule, HttpModule]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectSummaryAuditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the ticket results of an audit', () => {
    expect(component).toBeTruthy();
  });
});
