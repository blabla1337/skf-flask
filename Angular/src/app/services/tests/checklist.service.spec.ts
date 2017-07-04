import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { ChecklistService } from "../../services/checklist.service";
import { async } from "@angular/core/testing";
import { Checklist } from "../../models/checklist";


describe('Checklist service', () => {
  let mockResponse, matchingItem, connection;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        ChecklistService,
        MockBackend,
        BaseRequestOptions,
        {
          provide: Http,
          useFactory: (backend, defaultOptions) => new Http(backend, defaultOptions),
          deps: [MockBackend, BaseRequestOptions]
        },
         //{ provide: XHRBackend, useClass: MockBackend }        
      ]
    });

   const items = [
    {
      "checklist_items_checklistID": "1.1",
      "checklist_items_content": "Verify that all application components are identified and are known to be needed",
      "checklist_items_level": 1,
      "kb_item_title": "identify all application components",
      "kb_items_content": " Identify all application components\n\n\n Description:\n\nWhen you are building an application you first want to map where you are placing\nsource files, libraries and executables.\n\nWith these components identified and mapped, it becomes transparent where possible\npitfalls might be in your application and increases the maintainability of the\nsystem. Also, you have an indicator where possible reinforcements have to be\nimplemented to avoid attacks.(i.e places where your application contains executable's)\n\n Solution:\n\nVerify that all application components (either individual or groups of source files,\nlibraries, and/or executables) that are present in the application are identified.\n\nWhen you identified these components you may want to map and document them in order to\nhave a quick reference to this infrastructure when needed.\n"
    },
    {
      "checklist_items_checklistID": "1.10",
      "checklist_items_content": "Verify that there is no sensitive business logic, secret keys or other proprietary information in client side code.",
      "checklist_items_level": 2,
      "kb_item_title": "Sensitive information stored alongside the source code",
      "kb_items_content": " Sensitive information stored alongside the source code\n\n\n Description:\n\nSometimes when developing an application a programmer stores a password or other\ncredentials into the sourcecode as a comment for other developers to\nlogin into the application. When these comments still exist in a live environment,\nan attacker could use these credentials to gain access to the system.\n\n Solution:\n\nSearch your source code for comments which contains possible usercredentials.\nYou should also verify that there are no secrets and API keys are included in the\nsource code, or end up within the resulting binary.\n\nThis also applies to providing information about business logic and other critically sensitive\ninformation. Verify that there is no sensitive business logic, secret keys or other\nproprietary information in client side code.\n"
    }
    ];
    
   mockResponse = new Response(new ResponseOptions({body: {items}}));

  });

  describe('Get checklists by level {id}', () => {
    //Subscribing to the connection and storing it for later
    it('should return all the items', inject([ChecklistService, MockBackend], (service: ChecklistService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponse);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/checklist/level/1");
      });

      service.getChecklistLvl(1)
        .subscribe((items: Checklist[]) => {
         expect(items.length).toBe(2);
         expect(items[0]['checklist_items_checklistID']).toMatch("1.1");
        });
    }));
  });

  describe('Get all checklists items', () => {
  //Subscribing to the connection and storing it for later
  it('should return all the items', inject([ChecklistService, MockBackend], (service: ChecklistService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {
      connection.mockRespond(mockResponse);
      expect(connection.request.method).toEqual(RequestMethod.Get);
      expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
      expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/checklist/items");
    });

    service.getChecklist()
      .subscribe((items: Checklist[]) => {
        expect(items.length).toBe(2);
        expect(items[1]['kb_item_title']).toMatch("Sensitive information stored alongside the source code");
      });
    }));
  });

  describe('Get a checklist item', () => {
  //Subscribing to the connection and storing it for later
  it('should return one item', inject([ChecklistService, MockBackend], (service: ChecklistService, backend: MockBackend) => {
    backend.connections.subscribe(connection => {
      connection.mockRespond(mockResponse);
      expect(connection.request.method).toEqual(RequestMethod.Get);
      expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
      expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/checklist/1");
    });

    service.getChecklistItem(1)
      .subscribe((items: Checklist[]) => {
        expect(items.length).toBe(2);
        expect(items[1]['kb_item_title']).toMatch("Sensitive information stored alongside the source code");
      });
    }));
  });
  
});