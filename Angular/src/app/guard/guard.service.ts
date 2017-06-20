import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AppSettings } from '../globals';

@Injectable()
export class GuardService implements CanActivate {

    constructor(private router: Router) { }

    canActivate() {
        if (AppSettings.AUTH_TOKEN) {
            // logged in so return true
            return true;
        }

        // not logged in so redirect to login page
        this.router.navigate(['/login']);
        return false;
    }
}

//probeer canActivate method per privilege