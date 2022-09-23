import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { OAuthService } from 'angular-oauth2-oidc';
import { OAuthErrorEvent } from 'angular-oauth2-oidc'
import { UserService } from '../../core/services/user.service';
import { environment } from '../../../environments/environment';
import { HttpErrorResponse } from '@angular/common/http';

@Injectable()
export class LoggedInAuthGuard implements CanActivate {

    constructor(
        private router: Router,
        private oauthService: OAuthService,
        private _UserService: UserService,
        ) { }

    canActivate(): boolean {
        if(environment.AUTH_METHOD == "skiploginprovider"){
            return true
        }


        if(environment.AUTH_METHOD == "openidprovider"){
            this._UserService
            .getActive()
            .subscribe((response) => {
                // This is success
            },
            (error: HttpErrorResponse) => {
                // Handle error
                // Use if conditions to check error code, this depends on your api, how it sends error messages
                this.router.navigate(["/auth/login"])
            });
            return true
        }
    }
}
