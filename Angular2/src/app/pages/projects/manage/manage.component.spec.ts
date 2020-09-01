import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjectManageComponent } from './manage.component';

describe('ProjectManageComponent', () => {
  let component: ProjectManageComponent;
  let fixture: ComponentFixture<ProjectManageComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProjectManageComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectManageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
