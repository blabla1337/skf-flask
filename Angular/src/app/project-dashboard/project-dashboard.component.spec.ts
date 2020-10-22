import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, FormControl, NgForm } from '@angular/forms';
import { OrderBy } from '../pipes/order-by.pipe'
import { HttpModule } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { fakeAsync } from '@angular/core/testing';
import { StartsWithPipe } from '../pipes/starts-with.pipe';
import { ProjectDashboardComponent } from './project-dashboard.component';
import { Sprint } from '../models/sprint';
import { RouterTestingModule } from '@angular/router/testing';
import { SprintService } from '../services/sprint.service';


describe('Knowledgebase component component', () => {
    let component: ProjectDashboardComponent;
    let fixture: ComponentFixture<ProjectDashboardComponent>;
    let debugElement: DebugElement;
    let htmlElement: HTMLElement;
    const questions: Sprint[] = [];

    questions.push({ 'project_id': 1, 'question_pre_ID': '1', 'result': 'True' })
    questions.push({ 'project_id': 1, 'question_pre_ID': '2', 'result': 'False' })

    const mockQuestionService = Observable.of(questions)
    const mockSprintService = Observable.of(1);

    beforeEach(async () => {
        TestBed.configureTestingModule({
            declarations: [ProjectDashboardComponent, OrderBy, StartsWithPipe],
            imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
            providers: [
                SprintService,
            ],
        }).compileComponents();
    })


    beforeEach(() => {
        fixture = TestBed.createComponent(ProjectDashboardComponent)
        component = fixture.componentInstance;
        debugElement = fixture.debugElement.query(By.css('section'));
        fixture.detectChanges()
        component.idFromURL = 1;
        component.steps = false;
    })

    it('Newsprint should return errors if form is not filled in correctly', fakeAsync(() => {
        component.newSprint();
        expect(component.return).toBeFalsy()
        expect(component.errors).toMatch('Sprint name was empty!')
        expect(component.errors).toMatch('Sprint description was empty!')
    }))


    it('should check if goes through new sprint', () => {
        component.sprint_name = 'name';
        component.sprint_descriptionription = 'foobar'
        component.newSprint();
        fixture.detectChanges();
        expect(component.steps).toBeTruthy();
    })

    it('should check if goes through false delete!', () => {
        const deleter = component.deleter(1);
        expect(deleter).toBeFalsy()
    })

    it('Invoke the Modal open for better score! :-p', fakeAsync(() => {
        component.canEdit = true;
        spyOn(component, 'open');
        fixture.detectChanges(); // update view with quote
        const btnEle = fixture.debugElement.nativeElement.querySelector('.intro button');
        btnEle.click();
        expect(component.open).toHaveBeenCalled();
    }));

    it('check if component compiles succesfully', () => {
        expect(component).toBeTruthy();
    });
})


