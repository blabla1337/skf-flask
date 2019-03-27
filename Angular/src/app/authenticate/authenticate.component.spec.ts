import { ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from "@angular/platform-browser";
import { DebugElement } from "@angular/core";
import { AuthenticateComponent } from "./authenticate.component";
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from "@angular/http";
import { RouterTestingModule } from "@angular/router/testing";
import { AuthenticateService } from "../services/authenticate.service";
import { Observable } from "rxjs/Observable";
import {
  SocialLoginModule,
  AuthServiceConfig,
  GoogleLoginProvider,
} from "angular-6-social-login";

// Configs 
export function getAuthServiceConfigs() {
  
  let config = new AuthServiceConfig(
      [
        {
          id: GoogleLoginProvider.PROVIDER_ID,
          provider: new GoogleLoginProvider("")
          // Provide the google API client_id inside GoogleLoginProvider() i.e GoogleLoginProvider("YOUR_GOOGLE_API")
        }
      ]
  );
  return config;
  }
describe("Testing the Authenticate component", () => {

  let authenticateComponent: AuthenticateComponent;
  let authenticateComponentFixture: ComponentFixture<AuthenticateComponent>;
  let textDebugElement: DebugElement;
  let textElement: HTMLElement;

  let mockService = Observable.of({ "Authorization token": "dummy token", "username": "admin" });
  beforeEach(() => {

    // Use TestBed to configure module for the tests below
    TestBed.configureTestingModule({
      // We declare only our authenticateComponent
      declarations: [AuthenticateComponent],
      imports: [NgbModule.forRoot(), FormsModule, HttpModule, RouterTestingModule,SocialLoginModule],
      providers: [{ provide: AuthenticateService, useClass: mockService },{
        provide: AuthServiceConfig,
        useFactory: getAuthServiceConfigs
      }]
    });

    // Use TestBed to create ComponentFixture for our authenticateComponent:
    authenticateComponentFixture = TestBed.createComponent(AuthenticateComponent);
    // Access authenticateComponent instance:AuthenticateComponent
    authenticateComponent = authenticateComponentFixture.componentInstance;
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