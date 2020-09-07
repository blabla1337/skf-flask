import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { RouterTestingModule } from '@angular/router/testing';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';

import { StringFilterPipe } from '../../../core/pipes/stringfilter.pipe'
import { ManageComponent } from './manage.component';

describe('ManageComponent', () =>
{
    let component: ManageComponent;
    let fixture: ComponentFixture<ManageComponent>;

    beforeEach(async(() =>
    {
        TestBed.configureTestingModule({
            imports: [ReactiveFormsModule, FormsModule, HttpClientTestingModule, RouterTestingModule],
            declarations: [ManageComponent, StringFilterPipe]
        })
            .compileComponents();
    }));

    beforeEach(() =>
    {
        fixture = TestBed.createComponent(ManageComponent);
        component = fixture.componentInstance;
        component.ngOnInit();
        fixture.detectChanges();
    });

    it('should create', () =>
    {
        expect(component).toBeTruthy();
    });

    it('should valid submit', () =>
    {
        component.validSubmit();
        expect(component.submit).toBeTruthy();
    });

    it('should grant user', () =>
    {
        component.accountUserGrant(1);
    });

    it('should revoke user', () =>
    {
        component.accountUserRevoke(1);
    });

    it('should give access', () =>
    {
        component.accountUserPrivilege('admin', 1);
    });
});
