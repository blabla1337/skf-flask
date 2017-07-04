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
  const items = [
    {
      "Authorization token": "test token",
      "username": "user",
    }
  ];

  const firstLogin =
    {
      accessToken: 1234,
      email: "test@test.com",
      password: "password",
      repassword: "repassword",
      username: "admin"
    }

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
    mockResponse = new Response(new ResponseOptions({ body: { items } }));

  });

  it("isLoggedIn should return false after creation",
    inject([AuthenticateService], (service: AuthenticateService) => {
      expect(service.isLoggedIn()).toBeFalsy();
    }));

  it("logout should return false after invoking",
    inject([AuthenticateService], (service: AuthenticateService) => {
      expect(service.logout()).toBeFalsy();
    }));

  //Subscribing to the connection and storing it for later
  it('Test authentication function, request method, endpoint, variables & headers', inject([AuthenticateService, MockBackend], (service: AuthenticateService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {
      connection.mockRespond(mockResponse);
      expect(connection.request.method).toEqual(RequestMethod.Post);
      expect(connection.request.text()).toEqual(JSON.stringify({ username: "admin", password: "admin" }));
      expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
      expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/user/login");
    });

    service.authenticate("admin", "admin")
      .subscribe((response) => {
        expect(response).toEqual({ items });
      });
  }));

  //Subscribing to the connection and storing it for later
  it('Test user activation request method, endpoint, variables & headers', inject([AuthenticateService, MockBackend], (service: AuthenticateService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {

      expect(connection.request.method).toEqual(RequestMethod.Put);
      expect(connection.request.text()).toEqual(JSON.stringify(firstLogin));
      expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
      expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/user/activate/1");
    });

    service.activateUser("test@test.com", "admin", "1234", "password", "repassword", 1)
      .subscribe(() => {
   });
  }));

});
