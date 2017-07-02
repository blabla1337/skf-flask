import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from "@angular/platform-browser";
import { DebugElement } from "@angular/core";
import { AuthenticateComponent } from "./authenticate.component";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from "@angular/http";
import { RouterTestingModule } from "@angular/router/testing";

describe("Testing the Authenticate component", () => {

  let authenticateComponent: AuthenticateComponent;
  let authenticateComponentFixture: ComponentFixture<AuthenticateComponent>;
  let textDebugElement: DebugElement;
  let textElement: HTMLElement;

  beforeEach(() => {

    // Use TestBed to configure module for the tests below
    TestBed.configureTestingModule({
      // We declare only our authenticateComponent
      declarations: [AuthenticateComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule]
    });

    // Use TestBed to create ComponentFixture for our authenticateComponent:
    authenticateComponentFixture = TestBed.createComponent(AuthenticateComponent);
    // Access authenticateComponent instance:AuthenticateComponent
    authenticateComponent = authenticateComponentFixture.componentInstance;

    // We need to pass a Predicate to .query() - in our case it's By.css() where we pass a CSS selector.
    //textDebugElement = authenticateComponentFixture.debugElement.query(By.css("span"));
    // This is our <h2> element that contains the displayed text:
    // textElement = textDebugElement.nativeElement;
  });

  it("should provide username error if not filled in", () => {
    authenticateComponent.username = "admin"
    authenticateComponent.onLogin();
    expect(authenticateComponent.error).toMatch("password")
  });

  it("should provide password error if not filled in", () => {
    authenticateComponent.password = "admin"
    authenticateComponent.onLogin();
    expect(authenticateComponent.error).toMatch("username")
  });

  it('should create the authenticate component', () => {
    expect(authenticateComponent).toBeTruthy();
  });
});