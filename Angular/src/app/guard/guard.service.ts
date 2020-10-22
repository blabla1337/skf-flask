import { Injectable } from '@angular/core';
import { Router, CanActivate } from '@angular/router';
import { AppSettings } from '../globals';

@Injectable()
export class GuardService implements CanActivate {

    constructor(private router: Router) { }
    public returner: boolean;
    canActivate() {
        if (AppSettings.AUTH_TOKEN || AppSettings.SKIP_LOGIN) {
            // logged in so return true
            this.returner = true;
            return this.returner
        }

        // not logged in so redirect to login page
        this.router.navigate(['/login']);
         this.returner = false;
            return this.returner
    }
}

// probeer canActivate method per privilege
