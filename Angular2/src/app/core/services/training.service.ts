import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Course} from '../models/course.model';
import {Observable, of} from 'rxjs';
import _ from "lodash";

@Injectable()
export class TrainingService {
  constructor(
    private http: HttpClient,
  ) { }

  // TODO IB this should be by courseId
  seenItems: string[] = [];

  // TODO IB !!!! test this
  setCourseSeenItems(courseId: string, itemIds: string[]): Observable<boolean> {
    this.seenItems.push(...itemIds)
    this.seenItems = _.uniq(this.seenItems)
    return of(true)
  }

  // TODO IB !!!! test this
  getCourseSeenItems(courseId: string): Observable<string[]> {
    return of(this.seenItems)
  }

  getCourse(courseId: string): Observable<Course> {
    return of(TrainingService.getSampleCourse());
  }

  private static getSampleCourse(): Course {
    return {
      "id": "84c62728-c371-4d51-adb5-21a53d366474",
      "version": 2.1,
      "date": "25/02/2022",
      "name": "Secure Development",
      "languages": [
        "python",
        "java",
        "js",
        "net"
      ],
      "content": [
        {
          "slide": "skf/markdown/learning_platform/slides/1.md"
        }
      ],
      "topics": [
        {
          "id": "c2aeef96-4d64-4360-a16a-95e32c1c5a5c",
          "name": "Session management",
          "content": [
            {
              "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
          ],
          "categories": [
            {
              "id": "bd87bbcd-2fc5-4619-a782-9aa6400a3d4d",
              "name": "Session Hijacking",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/1.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/1.md"
                },
                {
                  "lab": {
                    "hint": "This is a super simple tip & hint!",
                    "writeup": "https://owasp-skf.gitbook.io/asvs-write-ups/server-side-template-injection-ssti",
                    "images": [
                      {
                        "python": "blabla1337/owasp-skf-lab-py"
                      },
                      {
                        "java": "blabla1337/owasp-skf-lab-java"
                      },
                      {
                        "js": "blabla1337/owasp-skf-lab-js"
                      },
                      {
                        "net": "blabla1337/owasp-skf-lab-net"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "id": "ac1eb377-7e5f-4eae-9757-45f9c8b3b058",
              "name": "HTTP Only flag",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/2.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/2.md"
                }
              ]
            },
            {
              "id": "6d102708-f900-4665-98c6-9efb3ac56fb4",
              "name": "Session riding",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/3.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/3.md"
                }
              ]
            }
          ]
        },
        {
          "id": "0f62ea67-476f-46d2-956d-110546492ab3",
          "name": "Validation, Sanitization and Encoding",
          "content": [
            {
              "video": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            }
          ],
          "categories": [
            {
              "id": "cd08670b-64fe-412a-92cb-6e5dac00959e",
              "name": "SQL injection",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/4.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/4.md"
                }
              ]
            },
            {
              "id": "905b38c5-54a3-4b82-985e-b9812a2c9ce4",
              "name": "LDAP injection",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/5.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/5.md"
                }
              ]
            },
            {
              "id": "218b1d8e-803b-4fc1-b05a-e7ce4a0daae2",
              "name": "Server Side Template injection",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/6.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/6.md"
                }
              ]
            },
            {
              "id": "c04099d4-ee8d-4c35-adc7-8f4a5a98a49e",
              "name": "Server Side Template injection",
              "content": [
                {
                  "slide": "skf/markdown/learning_platform/secure_code/slides/7.md"
                },
                {
                  "questionnaire": "skf/markdown/learning_platform/secure_code/questionnaire/7.md"
                }
              ]
            }
          ]
        }
      ]
    }
  }
}
