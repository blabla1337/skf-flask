import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjectSummaryAuditComponent } from './project-summary-audit.component';

describe('ProjectSummaryComponent', () => {
  let component: ProjectSummaryAuditComponent;
  let fixture: ComponentFixture<ProjectSummaryAuditComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProjectSummaryAuditComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectSummaryAuditComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
