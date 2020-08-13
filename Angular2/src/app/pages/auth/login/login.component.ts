import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

import { AuthService } from '../../../core/services/auth.service';

@Component({ templateUrl: 'login.component.html' })
export class LoginComponent implements OnInit
{

    year: number = new Date().getFullYear();
    public isSubmitted: boolean;
    public loginForm: FormGroup;
    public skip: boolean;
    public token: any;
    public errormsg = false;
    public expired = false;

    constructor(
        // tslint:disable-next-line: variable-name
        private _authService: AuthService,
        private router: Router,
        private formBuilder: FormBuilder) { }

    ngOnInit()
    {
        this.loginForm = this.formBuilder.group({
            username: ['', Validators.required],
            password: ['', Validators.required],
        });

        if (localStorage.getItem('session') === 'expired') {
            this.expired = true;
        }
        localStorage.clear();
        sessionStorage.clear()
        localStorage.setItem('categorySelector', '1');
    }

    onLogin()
    {
        this.isSubmitted = true;
        if (this.loginForm.invalid) {
            this.errormsg = true;
            return;
        }
        this._authService.LoginSKFprovider(this.loginForm.value).subscribe(token =>
        {
            if (token['Authorization token']) {
                sessionStorage.setItem('Authorization', token['Authorization token']);
                // tslint:disable-next-line: no-string-literal
                sessionStorage.setItem('user', token['username']);
                this.router.navigate(['/dashboard']);
            }
        },
            () => this.errormsg = true);
    }

    onSkip()
    {
        this.skip = true;
        this.router.navigate(['/dashboard']);
    }

    onRegister()
    {
        this.router.navigate(['/auth/register']);
    }
}
