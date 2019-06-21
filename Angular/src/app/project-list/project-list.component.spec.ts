import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule } from '@angular/forms';
import { OrderBy } from '../pipes/order-by.pipe'
import { HttpModule } from '@angular/http';
import { Observable } from 'rxjs/Observable';

import { fakeAsync } from '@angular/core/testing';
import { tick } from '@angular/core/testing';
import { ProjectListComponent } from './project-list.component';
import { Project } from '../models/project';
import { ProjectService } from '../services/project.service';
import { RouterTestingModule } from '@angular/router/testing';



describe('Knowledgebase component component', () => {
  let component: ProjectListComponent;
  let fixture: ComponentFixture<ProjectListComponent>;
  let debugElement: DebugElement;
  let htmlElement: HTMLElement;
  const stub: Project[] = [{ name: 'test stub name', version: '1.1', description: 'description', level: 'test stub level' }]
  const mockService = Observable.of(stub);

  beforeEach(async () => {
    TestBed.configureTestingModule({
      declarations: [ProjectListComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
      providers: [{ provide: ProjectService, useClass: mockService }]
    }).compileComponents();
  })

  beforeEach(() => {
    fixture = TestBed.createComponent(ProjectListComponent)
    component = fixture.componentInstance;
    debugElement = fixture.debugElement.query(By.css('section'));
    fixture.detectChanges()
  })

  it('Knowledgebase items should be reflected in the html', () => {
    component.projects = stub;
    component.ngOnInit();
    fixture.detectChanges(); // update view with quote
    expect(debugElement.nativeElement.textContent).toMatch('test stub level');
  });


  it('check if component compiles succesfully', () => {
    component.error = 'I am a mocked error';
    fixture.detectChanges();
    expect(debugElement.nativeElement.textContent).toMatch('I am a mocked error');
  });

   it('check if component compiles succesfully', () => {
     component.open('Test modal')
     fixture.detectChanges();
   });

      it('check if component compiles succesfully', () => {
      component.projects = stub;
      component.delete = 'DELETES';
      fixture.detectChanges();
      component.deleter(1);
   });

  it('check if component compiles succesfully', () => {
    expect(component).toBeTruthy();
  });
})

