import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";
import { RouterTestingModule } from "@angular/router/testing";
import { AppModule } from "../../app.module";
import { UserAddService } from "../user-add.service";
import { User } from "../../models/user";
import { UserService } from "../user-manage.service";

describe('User-manage service', () => {
  let mockResponseMessage, mockResponseItems, matchingItem, connection;

  const message = [
    {
      "message": "string"
    }]

  const items = [{
    "access": "True",
    "activated": "True",
    "email": "example@owasp.org",
    "userID": 1,
    "userName": "admin"
  },
  {
    "access": "True",
    "activated": "True",
    "email": "user@owasp.org",
    "userID": 2,
    "userName": "user"
  }
  ]

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        UserService,
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

    mockResponseItems = new Response(new ResponseOptions({ body: { items } }));
    mockResponseMessage = new Response(new ResponseOptions({ body: { message } }));

  });

  //Subscribing to the connection and storing it for later
  it('Test authentication function, request method, endpoint, variables & headers', inject([UserService, MockBackend], (service: UserService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {
      connection.mockRespond(mockResponseMessage);
      expect(connection.request.method).toEqual(RequestMethod.Put);
      expect(connection.request.text()).toEqual(JSON.stringify({ active: "True" }));
      expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
      expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/user/manage/1");
    });

    service.grant(1)
      .subscribe((response) => {
        expect(response).toMatch(JSON.stringify([{ "message": "string" }]));
      });
  }));

    it('Test authentication function, request method, endpoint, variables & headers', inject([UserService, MockBackend], (service: UserService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {
      connection.mockRespond(mockResponseMessage);
      expect(connection.request.method).toEqual(RequestMethod.Put);
      expect(connection.request.text()).toEqual(JSON.stringify({ active: "False" }));
      expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
      expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/user/manage/1");
    });

    service.revoke(1)
      .subscribe((response) => {
        expect(response).toMatch(JSON.stringify([{ "message": "string" }]));
      });
  }));

      it('should return all the users', inject([UserService, MockBackend], (service: UserService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseItems);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/user/list");
      });

      service.getUsers()
        .subscribe((items) => {
         expect(items.length).toBe(2);
         expect(items[0]['email']).toEqual('example@owasp.org');
        });
    }));


});
