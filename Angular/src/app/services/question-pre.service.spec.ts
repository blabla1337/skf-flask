import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";
import { RouterTestingModule } from "@angular/router/testing";
import { Question_pre } from "../../models/question_pre";
import { QuestionPreService } from "../questions-pre.service";

describe('Question-pre service', () => {
  let mockResponseList, mockResponseNew, matchingItem, connection;
  QuestionPreService
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        QuestionPreService,
        MockBackend,
        BaseRequestOptions,
        {
          provide: Http,
          useFactory: (backend, defaultOptions) => new Http(backend, defaultOptions),
          deps: [MockBackend, BaseRequestOptions]
        },
      ],
      imports: [RouterTestingModule]
    });

  });

  describe('Get list of pre questions', () => {
    const items = [
    {
      "id": 1,
      "question": "You have a blueprint for the design, architecture and validated this using ASVS?"
    },
    {
      "id": 2,
      "question": "You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?"
    }    
    ];

    mockResponseList = new Response(new ResponseOptions({body: {items}}));
    //Subscribing to the connection and storing it for later
    it('should return all the pre questions', inject([QuestionPreService, MockBackend], (service: QuestionPreService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseList);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/questions_pre/items");
      });

      service.getPreQuestions()
        .subscribe((items: Question_pre[]) => {
         expect(items.length).toBe(2);
         expect(items[1]['id']).toEqual(2);
         expect(items[1]['question']).toEqual("You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?");
        });
    }));
  });
  
  describe('New pre questions', () => {
   const items = [
    {
      "projectID": 1,
      "question_pre_ID": "1",
      "result": "True"
    },
    {
      "projectID": 1,
      "question_pre_ID": "2",
      "result": "False"
    }
    ];

    const items2 = [
      {
        "return": "Stored the pre questions"
      }
    ];

    mockResponseNew = new Response(new ResponseOptions({ body: { items2 } }));
    //Subscribing to the connection and storing it for later
    it('should store the pre questions results', inject([QuestionPreService, MockBackend], (service: QuestionPreService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseNew);
        expect(connection.request.method).toEqual(RequestMethod.Put);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.headers.get("Authorization")).toBeDefined;
        expect(connection.request.text()).toEqual(JSON.stringify({projectID: 1, question_pre_ID: 1, result: "True"}));
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/questions_pre/store");
      });

      service.newQuestion(1, 1, "True")
        .subscribe((items) => {
          expect(items).toEqual({items2})
        });
    }));
  });

});