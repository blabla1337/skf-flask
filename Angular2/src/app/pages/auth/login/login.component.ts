import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

import { AuthService } from '../../../core/services/auth.service';

@Component({ templateUrl: 'login.component.html' })
export class LoginComponent implements OnInit {

    year: number = new Date().getFullYear();

    successmsg = false;
    errormsg = false;
    skip = false;

    constructor(private authService: AuthService,
                private router: Router) { }

    ngOnInit() {
    }

    onLogin(loginForm: NgForm) {
        const token = this.authService.authUser(loginForm.value);
        if (token) {
            localStorage.setItem('token', token.userName);
            this.successmsg = true;
            this.router.navigate(['/dashboard']);
        } else {
            this.errormsg = true;
        }
    }

    onSkip() {
        this.skip = true;
        this.router.navigate(['/dashboard']);
    }

    onRegister() {
        this.router.navigate(['/auth/register']);
    }
}
