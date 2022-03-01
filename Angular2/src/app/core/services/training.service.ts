import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Course, CourseInfo, Profile} from '../models/course.model';
import {Observable, of} from 'rxjs';
import _ from "lodash";

@Injectable({providedIn: 'root'})
export class TrainingService {
  constructor(private http: HttpClient) { }

  // TODO IB !!!! move to persistence
  private seenItems: string[] = [];

  public getProfiles(): Observable<Profile[]> {
    return of(TrainingService.getSampleProfiles())
  }

  private static getSampleProfiles(): Profile[] {
    return [
      {
        id: "4a03cbe7-2aa9-4b16-b4d6-55d125a550f2",
        text: `This profile is dedicated for developers who want to learn secure development.
        This course is based on the ASVS and the secure coding principles to teach the best practices.`,
        iconClass: "bx-code-alt",
        startButtonText: "Secure development"
      },
      {
        id: "12902ddc-e189-4d8c-a7fb-dbc70c3e43dd",
        text: `This profile is dedicated for security pentesters who want to learn the the basics and advanced techniques
        of penetration testing for Web/API applications. This course is based on the OWASP WSTG and teach you how to perform a good quality penetrationt test.`,
        iconClass: "bx-shield",
        startButtonText: "Hacking"
      },
      {
        id: "67fbf0a6-2b00-4983-a48a-4b0c7f0cdb8c",
        text: `This profile is dedicated for Ops and Infra people who want to learn about the server hardening and security best practices.
        This course is based on the VulnHub materials and lessons to teach the best practices for server configurations and hardening.`,
        iconClass: "bx-slider-alt",
        startButtonText: "Infra/Ops"
      },
    ]
  }

  public getCourses(profileId: string): Observable<CourseInfo[]> {
    return of(TrainingService.getSampleCourses())
  }

  private static getSampleCourses(): CourseInfo[] {
    return [
      {
        id: "0b87c26b-ecdf-422d-8fb2-4302b15ea280",
        text: `Easy / Starting`,
        iconClass: "bx-code-alt",
        startButtonText: "Easy / Starting"
      },
      {
        id: "6a0f41a0-dd16-453e-a9ad-95b71e348051",
        text: `Competent`,
        iconClass: "bx-code-alt",
        startButtonText: "Competent"
      },
      {
        id: "8a786f96-7289-4603-baa0-749d25ed0f09",
        text: `Advanced`,
        iconClass: "bx-code-alt",
        startButtonText: "Advanced"
      },
    ]
  }

  public getCourse(courseId: string): Observable<Course> {
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

  // TODO IB !!!! test this
  public setCourseSeenItems(courseId: string, itemIds: string[]): Observable<boolean> {
    this.seenItems.push(...itemIds)
    this.seenItems = _.uniq(this.seenItems)
    return of(true)
  }

  // TODO IB !!!! test this
  public getCourseSeenItems(courseId: string): Observable<string[]> {
    return of(this.seenItems)
  }
}
