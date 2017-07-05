import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from "@angular/platform-browser";
import { DebugElement } from "@angular/core";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from "@angular/http";
import { RouterTestingModule } from "@angular/router/testing";
import { Observable } from "rxjs/Observable";
import { ProjectService } from "../services/project.service";
import { ProjectSummaryAuditComponent } from "./project-summary-audit.component";





describe("project new component", () => {

  let component: ProjectSummaryAuditComponent;
  let componentFixture: ComponentFixture<ProjectSummaryAuditComponent>;
  let textDebugElement: DebugElement;
  let textElement: HTMLElement;

  let mockService = Observable.of({ "Authorization token": "dummy token", "username": "admin" });
  beforeEach(() => {

    // Use TestBed to configure module for the tests below
    TestBed.configureTestingModule({
      // We declare only our authenticateComponent
      declarations: [ProjectSummaryAuditComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule],
      providers: [{ provide: ProjectService, useClass: mockService }]
    });

    // Use TestBed to create ComponentFixture for our authenticateComponent:
    componentFixture = TestBed.createComponent(ProjectSummaryAuditComponent);
    // Access authenticateComponent instance:AuthenticateComponent
    component = componentFixture.componentInstance;
  });

  it("check errors if params not filled", () => {
    component.select("test");
    expect(component.selector).toMatch('test');
  });

   it("check errors if params not filled", () => {
    component.save(1,"checklist String");
    expect(component.succes).toBeUndefined()
  });

     it("check errors if params not filled", () => {
    component.fetchComment("1.1");
    expect(component.error).toMatch("")
    expect(component.succes).toMatch("")
    expect(component.comment).toMatch("")
  });
});