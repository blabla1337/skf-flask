import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";
import { Knowledgebase } from "../../models/knowledgebase";
import { KnowledgebaseService } from "../knowledgebase.service";

describe('Knowledge base service', () => {
  let mockResponse, matchingItem, connection;
  KnowledgebaseService
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        KnowledgebaseService,
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
      "content": " Filename Injection / Path Traversal\n\n\n Description:\n\nA Path Traversal attack aims to access files and directories that are stored outside the web root folder. By browsing the application, the attacker looks for absolute links to files stored on the web server. By manipulating variables that reference files with dotdotslash (../); sequences and its variations, it may be possible to access arbitrary files and directories stored on file system, including application source code, configuration, and critical system files, limited by system operational access control.\nThe attacker uses  ../../ sequences to move up to root directory, thus permitting navigation through the file system. This attack can be executed with an external malicious code injected on the path, like the Resource Injection attack.\n\n\n Solution:\n\nThe most effective solution to eliminate file inclusion vulnerabilities is to avoid passing\nusersubmitted input to any filesystem/framework API. If this is not possible the application\ncan maintain a white list of files, that may be included on the page, and then use an identifier\n(for example the index number) to access the selected file. Any request containing an invalid\nidentifier has to be rejected, in this way there is no attack surface for malicious users to\nmanipulate the path.\n\n",
      "kbID": 1,
      "title": "Filename injection Path traversel"
    },
    {
      "content": " XSS injection\n\n\n Description:\n\nEvery time the application gets userinput, whether this showing it on screen or processing\nthis data in the application background, these parameters should be escaped for malicious\ncode in order to prevent crosssite scripting injections.\nWhen an attacker gains the possibility to perform an XSS injection,\nhe is given the opportunity to inject HTML and JavaScript code directly into the\napplication. This could lead to accounts being compromised by stealing session cookies or directly affect the operation of the target application.\n\n Solution:\n\nIn order to prevent XSS injections, all userinput should be escaped or encoded.\nYou could start by sanitizing userinput as soon as it is inserted into the application,\nby preference using a so called whitelisting method.\nThis means you should not check for malicious content like the tags or anything,\nbut only allow the expected input. Every input which is outside of the intended operation\nof the application should immediately be detected and login rejected.\n\nThe second step would be encoding all the parameters or userinput before putting this in\nyour html with encoding libraries specially designed for this purpose.\n\nYou should take into consideration that there are several contexts for encoding userinput for\nescaping XSS injections. These contexts are amongst others:\n\nHTML encoding is for whenever your userinput is displayed directly into your HTML.\nHTML attribute encoding is the type of encoding/escaping that should be applied whenever your user input is displayed into the attribute of your HTML tags.\nHTML URL encoding ;This type of encoding/escaping should be applied to whenever you are using userinput into a HREF tag.\n\nJavaScript encoding should be used whenever parameters are rendered via JavaScript; your application will detect normal injections in the first instant. But your application still remains vulnerable to JavaScript encoding which will not be detected by the normal encoding/escaping methods.\n\n",
      "kbID": 3,
      "title": "xss injection"
    }
    ];
   mockResponse = new Response(new ResponseOptions({body: {items}}));

  });

    //Subscribing to the connection and storing it for later
    it('should return all the knowledgebase items', inject([KnowledgebaseService, MockBackend], (service: KnowledgebaseService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponse);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/kb/items");
      });

      service.getKnowledgeBase()
        .subscribe((items: Knowledgebase[]) => {
         expect(items.length).toBe(2);
         expect(items[0]['kbID']).toEqual(1);
        });
    }));
});