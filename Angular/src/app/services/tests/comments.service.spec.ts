import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";
import { CommentService } from "../comment.service";
import { Comment } from '../../models/comment'
import { RouterTestingModule } from "@angular/router/testing";

describe('Checklist service', () => {
  let mockResponse, matchingItem, connection, mockResponse2;
  let sprintID = 1;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        CommentService,
        MockBackend,
        BaseRequestOptions,
        {
          provide: Http,
          useFactory: (backend, defaultOptions) => new Http(backend, defaultOptions),
          deps: [MockBackend, BaseRequestOptions]
        },
        //{ provide: XHRBackend, useClass: MockBackend }        
      ],
      imports: [RouterTestingModule]
    });
  });

  describe('Get comments by checklist id and sprint {id}', () => {
    const items = [
      {
        "checklistID": "10.13",
        "comment": "dsfdsfdsfdsfds",
        "date": "2017-06-30 13:07:55",
        "sprintID": 1,
        "status": 1,
        "userID": 1,
        "username": "admin"
      },
      {
        "checklistID": "10.13",
        "comment": "dsfsdfds",
        "date": "2017-06-30 13:05:49",
        "sprintID": 1,
        "status": 3,
        "userID": 1,
        "username": "admin"
      }
    ];
    mockResponse = new Response(new ResponseOptions({ body: { items } }));
    
    //Subscribing to the connection and storing it for later
    it('should return all the comment items', inject([CommentService, MockBackend], (service: CommentService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponse);
        expect(connection.request.method).toEqual(RequestMethod.Post);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/comment/items");
      });
      service.getComment("1", "1")
        .subscribe((items: Comment[]) => {
          expect(items.length).toBe(2);
          expect(items[0]['checklistID']).toMatch("10.13");
        });
    }));

  });

  describe('Should test the insert of new comments', () => {
    const items2 = [
      {
        "return": "success"
      }
    ];
    mockResponse2 = new Response(new ResponseOptions({ body: { items2 } }));
    //Subscribing to the connection and storing it for later
    it('should create a new comment item', inject([CommentService, MockBackend], (service: CommentService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponse2);
        expect(connection.request.method).toEqual(RequestMethod.Put);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.headers.get("Authorization")).toBeDefined;
        expect(connection.request.text()).toEqual(JSON.stringify({checklistID: "1.1", comment: "comment", sprintID: 1, status: 1}));
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/comment/new");
      });
      
      service.newComment("1.1", "comment", "1", 1)
        .subscribe((items) => {
          expect(items).toEqual({items2})
        });
    }));

  })
  
});