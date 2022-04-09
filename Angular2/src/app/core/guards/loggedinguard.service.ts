import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { OAuthService } from 'angular-oauth2-oidc';
import { OAuthErrorEvent } from 'angular-oauth2-oidc'
import { environment } from '../../../environments/environment';

@Injectable()
export class LoggedInAuthGuard implements CanActivate {

    constructor(
        private _router: Router,
        private oauthService: OAuthService,
        ) { }

    canActivate(): boolean {
        if(environment.AUTH_METHOD == "skiploginprovider"){
            return true
        }

        if(environment.AUTH_METHOD == "openidprovider"){
            this.oauthService.refreshToken();
            var decodedToken = localStorage.getItem('expires_at');
            var date = new Date();
            
            if (Number(decodedToken) < date.getTime()/1000) {
                window.location.assign("/auth/login");
            }
            return true
        }
    }
}
