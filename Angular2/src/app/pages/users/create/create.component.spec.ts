import { async, ComponentFixture, TestBed, tick, fakeAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { Location } from '@angular/common';

import { UserCreateComponent } from './create.component';
import { ManageComponent } from '../manage/manage.component';

describe('UserCreateComponent', () =>
{
    let component: UserCreateComponent;
    let fixture: ComponentFixture<UserCreateComponent>;
    let router: Router;
    let location: Location;

    beforeEach(async(() =>
    {
        TestBed.configureTestingModule({
            imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule,
                    RouterTestingModule.withRoutes([
                        { path: 'users/manage', component: ManageComponent },
                    ])],
            declarations: [UserCreateComponent]
        })
            .compileComponents();
        router = TestBed.inject(Router);
        location = TestBed.inject(Location);
        router.initialNavigation();
    }));

    beforeEach(() =>
    {
        fixture = TestBed.createComponent(UserCreateComponent);
        component = fixture.componentInstance;
        component.ngOnInit();
        fixture.detectChanges();
    });

    it('should create', () =>
    {
        expect(component).toBeTruthy();
    });

    it('should return true', () =>
    {
        component.validSubmit();
        expect(component.submit).toBeTruthy();
    });

    it('form invalid when empty', fakeAsync(() => {
        component.newUser();
        expect(component.userForm.invalid).toBeTruthy();

        router.navigate(['users/manage']);
        tick();
        expect(location.path()).toBe('/users/manage');
    }));

    it('priviledge field validity', () => {
        let priviledge = component.userForm.controls['privilege_id'];
        expect(priviledge.valid).toBeFalsy();

        let errors = {};
        errors = priviledge.errors || {};
        expect(errors['required']).toBeTruthy();
      });

});
