import { TestBed, fakeAsync, inject, tick } from '@angular/core/testing';
import { MockBackend } from '@angular/http/testing';
import { Http, BaseRequestOptions, Response, ResponseOptions, RequestMethod, XHRBackend } from '@angular/http';
import { Observable } from 'rxjs/Rx';
import { async } from "@angular/core/testing";

import { CodeExamplesService } from "../code-examples.service";
import { CodeExample } from "../../models/code-example";
import { RouterTestingModule } from "@angular/router/testing";


describe('Code examples service', () => {
  let mockResponse, matchingItem, connection;
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        CodeExamplesService,
        MockBackend,
        BaseRequestOptions,
        {
          provide: Http,
          useFactory: (backend, defaultOptions) => new Http(backend, defaultOptions),
          deps: [MockBackend, BaseRequestOptions]
        },
         //{ provide: XHRBackend, useClass: MockBackend }        
      ],
      imports:[RouterTestingModule]
    });

   const items = [
  {
      "codeID": 81,
      "code_lang": "php",
      "content": " File upload\n\n\n Example:\n\n\n\t<?php\n\n\tclass fileUpload{\n\t\tpublic function Image(){\n\n\t\t\tinclude('classes.php');\n\t\t\t$validated = new validate();\n\t\t\t$log = new logging();\n\n\n\t\t\t$image = $_FILES['fileToUpload'];\n\t\t\t//File location outside of the root\n\t\t\t$uploaddir = 'assets/uploads/';\n\n\t\t\t//check extensions\n\t\t\t$filetype = explode(\".\", $image['name']);\n\n\t\t\t/*\n\t\t\tFor uploading out of intended directory we check the filename and verify that it only contains alpahnumeric values.\n\t\t\t*/\n\t\t\tif($validated > inputValidation($filetype[0], \"alpanumeric\", \"invalid filename\", \"MOD\", 2){\n\t\t\t\theader('location:/page');\n\t\t\t\tdie();\n\t\t\t}\n\n\t\t\t/*\n\t\t\tWe take the last array value to make sure it is the last extension to prevent validating\n\t\t\t.jpg.php in a file name.\n\t\t\t*/\n\t\t\t$takeLastValue = count($filetype)  1;\n\n\t\t\twhile(($filetype[$takeLastValue] != \"png\") && ($filetype[$takeLastValue] != \"jpg\")){\n\n\t\t\t\t//Set a log for whenever there is an unexpected userinput with a threat level\n\t\t\t\t$log > setLog($_SESSION['userID'],\"Unrestricted image extension upload\",\n\t\t\t\t\"FAIL\", date(ddmmyyyy), $privilege, \"HIGH\");\n\n\t\t\t\t/*\n\t\t\t\tSet counter; if counter hits 3, the user's session must be terminated.\n\t\t\t\tAfter 3 session terminations the user account should be blocked\n\t\t\t\tSince the high threat level will lead to immediate session termination\n\t\t\t\t*/\n\t\t\t\t$log > setCounter(3);\n\n\t\t\t\t//The die function is to make sure the rest of the php code is not executed beyond this point\n\t\t\t\tdie();\n\t\t\t}\n\n\t\t\t // Check file size\n\t\t\tif($image[\"size\"] > 500000) {\n\t\t\t\t header('location:/page');\n\t\t\t\t die();\n\t\t\t }\n\n\t\t\t// Check if file already exists to prevent overwriting\n\t\t\tif(file_exists('assets/uploads/'.$image['name'])) {\n\t\t\t\theader('location:/page');\n\t\t\t\tdie();\n\t\t\t}  \n\n\t\t\t//if all goes well upload your file, first we want to log the event.\n\t\t\t$log > setLog($_SESSION['userID'],\"File upload\", \"SUCCESS\", date(ddmmyyyy),\n\t\t\t$privilege, \"NULL\");\n\n\t\t\t$uploadfile = $uploaddir . basename($image['name']);\n\t\t\tmove_uploaded_file($image['tmp_name'], $uploadfile);\n\n\t\t\t//Last mime type check after upload if not correct than delete!\n\t\t\t$finfo = finfo_open(FILEINFO_MIME_TYPE);\n\t\t\techo $theType = finfo_file($finfo, $uploaddir.$image['name']);\n\n\t\t\tif($theType != \"image/jpeg\" && $theType != \"image/png\"){    \n\t\t\t\tunlink($uploaddir.$image['name']);\n\n\t\t\t\t//Set a log for whenever there is unexpected userinput with a threat level\n\t\t\t\t$log > setLog($_SESSION['userID'],\"invalid image mime type\",\n\t\t\t\t\"FAIL\", date(ddmmyyyy), $privelige, \"HIGH\");\n\n\t\t\t\t/* ^^\n\t\t\t\tSet counter; if counter hits 3, the user's session must be terminated.\n\t\t\t\tAfter 3 session terminations the user account should be blocked\n\t\t\t\tsince the high threat level can lead to immediate session termination.\n\t\t\t\t*/\n\t\t\t\t$log > setCounter(3);\n\n\t\t\t\t//The die function is to make sure the rest of the php code is not executed beyond this point\n\t\t\t\tdie();              \n\t\t\t}\n\t\t}\n\t}\n\t?>\n",
      "title": "File upload"
    },
    {
      "codeID": 82,
      "code_lang": "php",
      "content": " Anti clickjacking headers\n\n\n Example:\n\n\n    /*\n  \tOne way to defend against clickjacking is to include a \"framebreaker\" script in each\n  \tpage that should not be framed. The following methodology will prevent a webpage from\n  \tbeing framed even in legacy browsers, that do not support the XFrameOptionsHeader.\n  \tIn the document HEAD element, add the following:\n  \tFirst apply an ID to the style element itself:\n  \t*/\n  \t<style id=\"antiClickjack\">body{display:none !important;}</style>\n\n  \t//And then delete that style by its ID immediately after in the script:\n\n      <script type=\"text/javascript\">\n  \t   if (self === top) {\n  \t\t   var antiClickjack = document.getElementById(\"antiClickjack\");\n  \t\t   antiClickjack.parentNode.removeChild(antiClickjack);\n  \t   } else {\n  \t\t   top.location = self.location;\n  \t   }\n      </script>\n\n\n  \t<?php\n    \n  \t/*\n  \tThe second option is to use \"security headers\".\n  \tThere are two options for setting the \"anticlickjacking\" headers in your application:\n  \t*/\n\n  \t//this will completely prevent your page from being displayed in an iframe.\n  \theader('XFrameOptions: DENY');\n\n\n  \t//this will completely prevent your page from being displayed in an iframe on other sites.\n  \theader('XFrameOptions: SAMEORIGIN');\n  \t?>\n",
      "title": "Anti clickjacking headers"
    }
    ];
   mockResponse = new Response(new ResponseOptions({body: {items}}));
  });

  describe('get the code examples by language', () => {
    //Subscribing to the connection and storing it for later
    it('should return all the code languages by language', inject([CodeExamplesService, MockBackend], (service: CodeExamplesService, backend: MockBackend) => {
      backend.connections.subscribe(connection => {
        connection.mockRespond(mockResponse);
        expect(connection.request.method).toEqual(RequestMethod.Get);
        expect(connection.request.headers.get("Content-Type")).toEqual("application/json");
        expect(connection.request.url).toEqual("http://127.0.0.1:8888/api/code/lang/php");
      });

      service.getCode('php')
        .subscribe((items: CodeExample[]) => {
         expect(items.length).toBe(2);
         expect(items[0]['codeID']).toMatch("81");
        });
    }));
  });
});