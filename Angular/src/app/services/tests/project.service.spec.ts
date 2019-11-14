import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { Project } from '../../models/project';
import { ProjectStats } from '../../models/project_stats';
import { ProjectService } from '../project.service';

describe('Project service', () => {
  let mockResponseList, mockResponseStats, mockResponseProject, mockResponseNew, mockResponseDelete, matchingItem, connection;
  ProjectService
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        ProjectService,
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

  describe('Get list of projects', () => {
    const items = [
    {
      'project_id': 1,
      'group_id': 1,
      'project_name': 'Project name app 1',
      'project_version': '1.1',
      'project_description': 'Project description of app 1',
      'timestamp': '1.1',
      'level': '3'
    },
    {
      'project_id': 2,
      'group_id': 1,
      'project_name': 'Project name app 2',
      'project_version': '2.2',
      'project_description': 'Project description of app 2',
      'timestamp': '1.1',
      'level': '3'
    }
    ];

    mockResponseList = new Response(new ResponseOptions({body: {items}}));
    // Subscribing to the connection and storing it for later
    it('should return all the projects', inject([ProjectService, MockBackend], (service: ProjectService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseList);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/project/items');
      });

      service.getProjects()
        .subscribe((items: Project[]) => {
         expect(items.length).toBe(2);
         expect(items[0]['project_id']).toEqual(1);
         expect(items[1]['project_name']).toEqual('Project name app 2');
        });
    }));
  });

  describe('Get stats of project', () => {
   const items = [
    {
      'project_id': 1,
      'project_name': 'Project name app 1',
      'project_desc': 'Project description of app 2',
      'project_level': 1,
      'project_open': 78,
      'project_closed': 12,
      'project_accepted': 34
    }
    ];

    mockResponseStats = new Response(new ResponseOptions({body: {items}}));
    // Subscribing to the connection and storing it for later
    it('should return stats of the project', inject([ProjectService, MockBackend], (service: ProjectService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseStats);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/project/stats/1');
      });

      service.getStats(1)
        .subscribe((items: ProjectStats[]) => {
         expect(items.length).toBe(1);
         expect(items[0]['project_id']).toEqual(1);
         expect(items[0]['project_accepted']).toEqual(34);
         expect(items[0]['project_name']).toEqual('Project name app 1');
        });
    }));
  });

  describe('Get project', () => {
   const items = [
    {
      'project_id': 3,
      'group_id': 1,
      'project_name': 'Project name app 3',
      'project_version': '1.1',
      'project_description': 'Project description of app 3',
      'timestamp': '1.1',
      'level': '3'
    },
    ];

    mockResponseProject = new Response(new ResponseOptions({body: {items}}));
    // Subscribing to the connection and storing it for later
    it('should return the project', inject([ProjectService, MockBackend], (service: ProjectService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseProject);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/project/1');
      });

      service.getProject(1)
        .subscribe((items: ProjectStats[]) => {
         expect(items.length).toBe(1);
         expect(items[0]['project_id']).toEqual(3);
         expect(items[0]['project_name']).toEqual('Project name app 3');
         expect(items[0]['level']).toEqual('3');
        });
    }));
  });

  describe('New project', () => {
   const items = [
    {
      'group_id': 1,
      'project_name': 'Project name app 3',
      'project_version': '1.1',
      'project_description': 'Project description of app 3',
      'timestamp': '1.1',
      'level': '3'
    },
    ];

    const items2 = [
      {
        'return': 'Created the project'
      }
    ];

    mockResponseNew = new Response(new ResponseOptions({ body: { items2 } }));
    // Subscribing to the connection and storing it for later
    it('should create a new project', inject([ProjectService, MockBackend], (service: ProjectService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseNew);
        expect(connection.request.method).toEqual(RequestMethod.Put);
        expect(connection.request.headers.get('Content-Type')).toEqual('application/json');
        expect(connection.request.headers.get('Authorization')).toBeDefined;
        expect(connection.request.text()).toEqual(JSON.stringify({name: 'Project name example', description: 'Project description example', version: '1.1'}));
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/project/new');
      });

      service.newProject('Project name example', 'Project description example', '1.1')
        .subscribe((items) => {
          expect(items).toEqual({items2})
        });
    }));
/*
    it('should update a project', inject([ProjectService, MockBackend], (service: ProjectService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseNew);
        expect(connection.request.method).toEqual(RequestMethod.Put);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.headers.get("Authorization")).toBeDefined;
        expect(connection.request.text()).toEqual(JSON.stringify({name: "Project name example", description: "Project description update", level: "1", version: "1.1"}));
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/project/update/1");
      });

      service.updateProject(1, "Project name example","Project description update", "1" ,"1.1")
        .subscribe((items) => {
          expect(items).toEqual({items2})
        });
    }));
*/

  });

  describe('Delete project', () => {
    const items2 = [
      {
        'return': 'Deleted the project'
      }
    ];

    mockResponseDelete = new Response(new ResponseOptions({ body: { items2 } }));
    // Subscribing to the connection and storing it for later
    it('should delete the project', inject([ProjectService, MockBackend], (service: ProjectService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponseDelete);
        expect(connection.request.method).toEqual(RequestMethod.Delete);
        expect(connection.request.headers.get('Content-Type')).toEqual('application/json');
        expect(connection.request.headers.get('Authorization')).toBeDefined;
        expect(connection.request.url).toEqual('http://127.0.0.1:8888/api/project/delete/1');
      });
      expect(service.delete(1)).toBeTruthy();
    }));
  });

});
