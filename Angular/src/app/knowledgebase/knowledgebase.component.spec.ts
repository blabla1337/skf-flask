import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { DebugElement } from '@angular/core'
import { KnowledgebaseComponent } from './knowledgebase.component';
import { Observable } from 'rxjs/Rx';
import { Knowledgebase } from '../models/knowledgebase';
import { HttpModule } from '@angular/http';
import { KnowledgebaseService } from "../services/knowledgebase.service";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { RouterTestingModule } from '@angular/router/testing';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { StartsWithPipe } from '../pipes/starts-with.pipe'
import { By } from "@types/selenium-webdriver";


describe('KnowledgebaseComponent', () => {
let fixture: ComponentFixture<KnowledgebaseComponent>;
let component : KnowledgebaseComponent;
let de : DebugElement;
let knowledgebaseService : KnowledgebaseService;
let knowledgebase : Knowledgebase[] = [{ id:1, title:"foobar", content:"foobar" }]
let htmlElement:HTMLElement;
let debugElement : DebugElement;
beforeEach(() => {
TestBed.configureTestingModule({
  imports:[HttpModule, FormsModule, NgbModule.forRoot()],
  declarations:[KnowledgebaseComponent, StartsWithPipe],
  providers:[KnowledgebaseService]
})

fixture = TestBed.createComponent(KnowledgebaseComponent)
component = fixture.componentInstance;
de = fixture.debugElement.nativeElement;
knowledgebaseService = TestBed.get(KnowledgebaseService)
});


it(`should test getKnowledgeItems to see if it gets filled by knowledbaseService`, () => {
  spyOn(knowledgebaseService, 'getKnowledgeBase').and.returnValue(Observable.of(knowledgebase))
  fixture.detectChanges()
  expect(component.knowledgeitems).toEqual(jasmine.objectContaining([{ id: 1, title:"foobar", content:"foobar" }]));
})

// it(`should test getKnowledgeItems to see if it fills the template with values`, () => {
//   spyOn(knowledgebaseService, 'getKnowledgeBase').and.returnValue(Observable.of(knowledgebase))
//   fixture.detectChanges()
// })

});
