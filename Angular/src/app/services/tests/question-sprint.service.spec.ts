import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Questions } from '../../models/questions';
import { QuestionsService } from '../questions.service';
import { Sprint } from '../../models/sprint';

describe('Question-sprint service', () => {
  let mockResponseList, mockResponseNew, matchingItem, connection;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        QuestionsService,
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
      'id': 1,
      'question': 'You have a blueprint for the design, architecture and validated this using ASVS?'
    },
    {
      'id': 2,
      'question': 'You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?'
    }
    ];

    mockResponseList = new Response(new ResponseOptions({body: {items}}));
    // Subscribing to the connection and storing it for later
    it('should return all the sprint questions', inject([QuestionsService, MockBackend], (service: QuestionsService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseList);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/questions/items/2');
      });

      service.getQuestions(2)
        .subscribe((items: Questions[]) => {
         expect(items.length).toBe(2);
         expect(items[1]['id']).toEqual(2);
         expect(items[1]['question']).toEqual('You have a blueprint for performing secure configuration, hardening of the application server and validated this using ASVS?');
        });
    }));
  });

  describe('New sprint questions', () => {

   const questions: Sprint[] = [];
   questions.push({'projectID': 1, 'question_pre_ID': '1', 'result': 'True'})
   questions.push({'projectID': 1, 'question_pre_ID': '2', 'result': 'False'})

    const items2 = {
        'return': 'Stored the sprint questions'
      }

    ;

    mockResponseNew = new Response(new ResponseOptions({ body: { items2 } }));
    // Subscribing to the connection and storing it for later
    it('should store the sprint questions results', inject([QuestionsService, MockBackend], (service: QuestionsService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseNew);
        expect(connection.request.method).toEqual(RequestMethod.Put);
        expect(connection.request.headers.get('Content-Type')).toEqual('application/json');
        expect(connection.request.headers.get('Authorization')).toBeDefined;
        expect(connection.request.text()).toEqual(JSON.stringify({questions}));
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/questions/store');
      });
      service.newSprint(questions)
        .subscribe((items) => {
          expect(items).toMatch(JSON.stringify([{return: 'Stored the sprint questions'}]))
        });
    }));
  });

});
