import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { AppModule } from '../../app.module';
import { UserAddService } from '../user-add.service';
import { User } from '../../models/user';

describe('User-add service', () => {
  let mockResponse, matchingItem, connection;
  const items: User[] = [{'accessToken': 1234, 'userID': 1}]

  const firstLogin = {
      email: 'test@test.com'
    }

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        UserAddService,
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

  // Subscribing to the connection and storing it for later
  it('Test authentication function, request method, endpoint, variables & headers', inject([UserAddService, MockBackend], (service: UserAddService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {
      connection.mockRespond(mockResponse);
      expect(connection.request.method).toEqual(RequestMethod.Put);
      expect(connection.request.text()).toEqual(JSON.stringify({ email: 'admin@admin.nl', privilege: 1 }));
      expect(connection.request.headers.get('Content-Type')).toEqual('application/json');
      expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/user/create');
    });

    service.newUser('admin@admin.nl', '1')
      .subscribe((response) => {
        expect(response).toMatch(JSON.stringify([{'accessToken': 1234, 'userID': 1}]));
      });
  }));

});
