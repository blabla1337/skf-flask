import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { UserUpdateComponent } from './update.component';

describe('UserUpdateComponent', () =>
{
    let component: UserUpdateComponent;
    let fixture: ComponentFixture<UserUpdateComponent>;

    beforeEach(waitForAsync(() =>
    {
        TestBed.configureTestingModule({
            imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
            declarations: [UserUpdateComponent]
        })
            .compileComponents();
    }));

    beforeEach(() =>
    {
        fixture = TestBed.createComponent(UserUpdateComponent);
        component = fixture.componentInstance;
        component.ngOnInit();
        fixture.detectChanges();
    });

    it('should create', () =>
    {
        expect(component).toBeTruthy();
    });
});
