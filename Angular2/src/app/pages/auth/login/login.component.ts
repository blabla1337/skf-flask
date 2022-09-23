import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

declare const eSheep: any;
import { OAuthService } from 'angular-oauth2-oidc';
import { environment } from '../../../../environments/environment';

@Component({ templateUrl: 'login.component.html' })


export class LoginComponent implements OnInit
{
    constructor(
        private oauthService: OAuthService,
        private router: Router,) { }

    public loginProvider = environment.AUTH_METHOD;

    ngOnInit(): void
    {
        localStorage.setItem("theme","light-theme.css")
        
        if(this.loginProvider == "skiploginprovider"){
            sessionStorage.setItem("access_token","")
            this.router.navigate(["/dashboard"])
        }
    }

    onLogin()
    {
        this.oauthService.initLoginFlow();
    }

    doBackdoor()
    {
        //eval()
        //system()
        //exec()
        //Nice i see you did some nice code reviewing to validate if the app is secure and doesn't contain backdoors?
        //Then You are freaking awesome! Please enjoy this little Easter-Egg for the hard word and good ethics!
        var pet = new eSheep();
        pet.Start();
        //Thanks to Adriano Petrucci (http://esheep.petrucci.ch) who created this little sheep.exe
    }
}
