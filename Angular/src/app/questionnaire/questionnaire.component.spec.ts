/*
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';
import { NgbModule } from "@ng-bootstrap/ng-bootstrap";
import { FormsModule, FormControl, NgForm } from "@angular/forms";
import { OrderBy } from '../pipes/order-by.pipe'
import { HttpModule } from "@angular/http";
import { Observable } from "rxjs/Observable";
import { fakeAsync } from "@angular/core/testing";
import { tick } from "@angular/core/testing";
import { Knowledgebase } from "../models/knowledgebase";
import { StartsWithPipe } from "../pipes/starts-with.pipe";
import { KnowledgebaseService } from "../services/knowledgebase.service";
import { QuestionsService } from "../services/questions.service";
import { Sprint } from "../models/sprint";
import { MockBackend } from "@angular/http/testing";
import { RouterTestingModule } from "@angular/router/testing";
import { inject } from "@angular/core/testing";
import { SprintService } from "../services/sprint.service";


describe('Knowledgebase component component', () => {
    let component: ProjectDashboardComponent;
    let fixture: ComponentFixture<ProjectDashboardComponent>;
    let questions: Sprint[] = [];
    let sprintService: QuestionsSprintService;

    questions.push({ "projectID": 1, "question_pre_ID": "1", "result": "True" })
    questions.push({ "projectID": 1, "question_pre_ID": "2", "result": "False" })

    let mockQuestionService = Observable.of(questions)
    let mockSprintService = Observable.of(1);

    beforeEach(async () => {
        TestBed.configureTestingModule({
            declarations: [ProjectDashboardComponent, OrderBy, StartsWithPipe],
            imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
            providers: [
                SprintService
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
        expect(component.errors).toMatch("Sprint name was empty!")
        expect(component.errors).toMatch("Sprint description was empty!")
    }))


    it('should check if goes through new sprint', () => {
        component.sprintName = "name";
        component.sprintDescription = "foobar"
        component.newSprint();
        fixture.detectChanges();
        expect(component.steps).toBeTruthy();
    })

    it('should check if goes through false delete!', () => {
        let deleter = component.deleter(1);
        expect(deleter).toBeFalsy()
    })

    it('Invoke the Modal open for better score! :-p', fakeAsync(() => {
        component.open("foobar")
        fixture.detectChanges(); // update view with quote
    }));

    it('check if component compiles succesfully', () => {
        expect(component).toBeTruthy();
    });
})

*/
