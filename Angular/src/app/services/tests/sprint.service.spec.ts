import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";
import { RouterTestingModule } from "@angular/router/testing";
import { Questions } from "../../models/questions";

import { Sprint } from "../../models/sprint";
import { SprintService } from "../sprint.service";
import { QuestionsService } from "../questions.service";


describe('Question-sprint service', () => {
  let mockResponseList, mockResponseNew, matchingItem, connection;
  
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        SprintService,
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

    //Subscribing to the connection and storing it for later
    it('should return all the sprint questions', inject([SprintService, MockBackend], (service: SprintService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseList);
        expect(connection.request.method).toEqual(RequestMethod.Delete);
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/sprint/delete/1");
      });

      service.delete(1)
        .subscribe(() => {
        });
    }));

});