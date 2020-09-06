import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { UserCreateComponent } from './create.component';

describe('UserCreateComponent', () =>
{
    let component: UserCreateComponent;
    let fixture: ComponentFixture<UserCreateComponent>;

    beforeEach(async(() =>
    {
        TestBed.configureTestingModule({
            imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
            declarations: [UserCreateComponent]
        })
            .compileComponents();
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

    it('form invalid when empty', () => {
        component.newUser();
        expect(component.userForm.invalid).toBeTruthy();
    });

    it('priviledge field validity', () => {
        let priviledge = component.userForm.controls['privilege_id'];
        expect(priviledge.valid).toBeFalsy();

        let errors = {};
        errors = priviledge.errors || {};
        expect(errors['required']).toBeTruthy();
      });

});
