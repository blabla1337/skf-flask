import { async, ComponentFixture, TestBed, tick, fakeAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

import { UpdateCodeComponent } from './update.component';
import { ViewCodeComponent } from '../view/view.component';

describe('UpdateCodeComponent', () =>
{
  let component: UpdateCodeComponent;
  let fixture: ComponentFixture<UpdateCodeComponent>;
  let router: Router;
  let location: Location;

  beforeEach(async(() =>
  {
    TestBed.configureTestingModule({
      imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule,
                RouterTestingModule.withRoutes([
                  { path: 'code-example/view', component: ViewCodeComponent },
                ])],
      declarations: [UpdateCodeComponent]
    })
      .compileComponents();
    router = TestBed.inject(Router);
    location = TestBed.inject(Location);
    router.initialNavigation();
  }));

  beforeEach(() =>
  {
    fixture = TestBed.createComponent(UpdateCodeComponent);
    component = fixture.componentInstance;
    component.ngOnInit();
    fixture.detectChanges();
  });

  it('should create', () =>
  {
    expect(component).toBeTruthy();
  });

  it('should update CodeExample Item', fakeAsync(() =>
  {
    component.updateCodeExampleItem();
    expect(component.isSubmitted ).toBeTruthy();
    expect(component.codeExampleForm.valid).toBeFalsy();

    router.navigate(['code-example/view']);
    tick();
    expect(location.path()).toBe('/code-example/view');
  }));
});
