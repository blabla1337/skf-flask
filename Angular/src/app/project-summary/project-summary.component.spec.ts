import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ProjectSummaryComponent } from './project-summary.component';
import { HttpModule } from '@angular/http';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterTestingModule } from '@angular/router/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


describe('ProjectSummaryComponent', () => {
  let component: ProjectSummaryComponent;
  let fixture: ComponentFixture<ProjectSummaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProjectSummaryComponent ],
      imports:[NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectSummaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create a summary of all sprints and pre development', () => {
    expect(component).toBeTruthy();
  });

  it('should call fetchComment', () => {
    spyOn(component, 'fetchComment');
    let btnEle = fixture.debugElement.nativeElement.querySelector('.content-panel > div');
    btnEle.click();
    expect(component.fetchComment).toHaveBeenCalled();
  });
});
