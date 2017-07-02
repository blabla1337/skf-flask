import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";
import { AuthenticateService } from "../authenticate.service";
import { RouterTestingModule } from "@angular/router/testing";
import { AppModule } from "../../app.module";

describe('Authenticate service', () => {
  let mockResponse, matchingItem, connection;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        AuthenticateService,
        MockBackend,
        BaseRequestOptions,

        {
          provide: Http,
          useFactory: (backend, defaultOptions) => new Http(backend, defaultOptions),
          deps: [MockBackend, BaseRequestOptions]
        },
        { provide: XHRBackend, useClass: MockBackend }
      ],
      imports: [RouterTestingModule]
    });

    const items = [
      {
        "authorization token": "dummy token ding",
        "username": "user",
      }
    ];
    mockResponse = new Response(new ResponseOptions({ body: { items } }));

  });

  describe('Test the Authenticate service settings', () => {

    it("isLoggedIn should return false after creation",
      inject([AuthenticateService], (service: AuthenticateService) => {
        expect(service.isLoggedIn()).toBeFalsy();
      }));

    it("logout should return false after invoking",
      inject([AuthenticateService], (service: AuthenticateService) => {
        expect(service.logout()).toBeFalsy();
      }));

    //Subscribing to the connection and storing it for later
    it('should return all the items', inject([AuthenticateService, MockBackend], (service: AuthenticateService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponse);
        expect(connection.request.method).toEqual(RequestMethod.Post);
        expect(connection.request.text()).toEqual(JSON.stringify({ username: "admin", password: "admin" }));
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/login");
      });
    }));
  });
});