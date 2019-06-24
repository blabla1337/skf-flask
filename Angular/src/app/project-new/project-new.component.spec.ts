import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterTestingModule } from '@angular/router/testing';
import { Observable } from 'rxjs/Observable';
import { ProjectService } from '../services/project.service';
import { ProjectNewComponent } from './project-new.component';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';


describe('project new component', () => {

  let component: ProjectNewComponent;
  let componentFixture: ComponentFixture<ProjectNewComponent>;
  let textDebugElement: DebugElement;
  let textElement: HTMLElement;

  const mockService = Observable.of({ 'Authorization token': 'dummy token', 'username': 'admin' });
  beforeEach(() => {

    // Use TestBed to configure module for the tests below
    TestBed.configureTestingModule({
      // We declare only our authenticateComponent
      declarations: [ProjectNewComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
      providers: [{ provide: ProjectService, useClass: mockService }]
    });

    // Use TestBed to create ComponentFixture for our authenticateComponent:
    componentFixture = TestBed.createComponent(ProjectNewComponent);
    // Access authenticateComponent instance:AuthenticateComponent
    component = componentFixture.componentInstance;
  });

  it('check errors if params not filled', () => {
    component.save();
    expect(component.error[0]).toMatch('Project name was left empty');
    expect(component.error[1]).toMatch ('Project version was left empty');
    expect(component.error[2]).toMatch ('Project description was left empty');
    expect(component.error[3]).toMatch ('Sprint name was left empty');
    expect(component.error[4]).toMatch('Sprint description was left empty');
  });

  it('returnpath is true if params are filled', () => {
    component.projectName = 'test';
    component.projectVersion = 'test';
    component.projectDescription = 'test';
    component.level = '1';
    component.sprintName = 'test';
    component.sprintDescription = 'test';
    spyOn(component, 'save');
    componentFixture.detectChanges(); // update view with quote
    const btnEle = componentFixture.debugElement.nativeElement.querySelector('.buttons .btn-success');
    btnEle.click();
    expect(component.save).toHaveBeenCalled();
    expect(component.error.length).toEqual(0);
  });

  it('test the invalid method should return true', () => {
    component.isInvalid()
    const test = component.isInvalid()
    expect(test).toBeTruthy();
  });

  it('should create the authenticate component', () => {
    expect(component).toBeTruthy();
  });
});
