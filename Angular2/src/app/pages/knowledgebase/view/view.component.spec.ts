import { async, ComponentFixture, TestBed, fakeAsync, tick } from '@angular/core/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { NgbNavModule } from "@ng-bootstrap/ng-bootstrap";
import { Router } from '@angular/router';
import { Location } from '@angular/common';

import { ViewKnowledebaseComponent } from './view.component';

describe('ViewKnowledebaseComponent', () =>
{
  let component: ViewKnowledebaseComponent;
  let fixture: ComponentFixture<ViewKnowledebaseComponent>;
  let router: Router;
  let location: Location;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule, NgbNavModule,
                RouterTestingModule.withRoutes([
                  { path: 'knowledgebase/view', component: ViewKnowledebaseComponent },
                ])],
      declarations: [ViewKnowledebaseComponent]
    })
      .compileComponents();
    router = TestBed.inject(Router);
    location = TestBed.inject(Location);
    router.initialNavigation();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(ViewKnowledebaseComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should navigate to knowledgebase/view on submit', fakeAsync(() =>
  {
    component.onSubmit();

    router.navigate(['knowledgebase/view']);
    tick();
    expect(location.path()).toBe('/knowledgebase/view');
  }));

  it('should login', () =>
  {
    component.loggedIn();
    expect(component.loggedIn).toBeTruthy();
  });
});
