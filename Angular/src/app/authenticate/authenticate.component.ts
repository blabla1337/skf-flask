import { Component, OnInit } from '@angular/core';
import { AuthenticateService } from '../services/authenticate.service';
import {
  AuthService,
  FacebookLoginProvider,
  GoogleLoginProvider
} from 'angular-6-social-login';

@Component({
  selector: 'app-authenticate',
  templateUrl: './authenticate.component.html',
  providers: [AuthenticateService]
})

export class AuthenticateComponent implements OnInit {
  public username: string;
  public password: string;
  public error: string[] = [];
  public return: boolean;
  public expired: boolean;
  public google_sign_in: boolean;
  
  constructor(public _authenticateService: AuthenticateService, private socialAuthService: AuthService) { }
  ngOnInit() {
    // To enable login with google set below variable as "this.google_sign_in=ture"
    this.google_sign_in = false;
    this.expired = false;
    if (localStorage.getItem('session') == "expired") { this.expired = true }
    localStorage.clear();
  }

  onLogin() {
    this.return = true;
    this.error = [];


    if (!this.username) { this.return = false; this.error.push("No username was provided"); }
    if (!this.password) { this.return = false; this.error.push("No password was provided"); }
    if (this.return == false) { return; }

    this._authenticateService.authenticate(this.username, this.password).subscribe(
      response => {
        if (response["Authorization token"] != "") {
          sessionStorage.setItem("auth_token", response["Authorization token"]);
          sessionStorage.setItem("user", response["username"]);
          location.replace("dashboard");
        } else { this.error.push("Wrong username/password combination!"); }
      })
  }

  skipLogin() {
    sessionStorage.setItem("skip_login", "true");
    location.replace("dashboard");
  }
  public socialSignIn(socialPlatform : string) {
    let socialPlatformProvider;
    if(socialPlatform == "google"){
      socialPlatformProvider = GoogleLoginProvider.PROVIDER_ID;
    }
    
    this.socialAuthService.signIn(socialPlatformProvider).then(
      (userData) => {
        // Now sign-in with userData
        this._authenticateService.google_authenticate(userData.token, userData.email).subscribe(
          response => {
            if (response["Authorization token"] != "") {
              sessionStorage.setItem("auth_token", response["Authorization token"]);
              sessionStorage.setItem("user", response["username"]);
              location.replace("dashboard");
            } else { this.error.push("Wrong username/password combination!"); }
          })
            
      }
    );
  }
}
