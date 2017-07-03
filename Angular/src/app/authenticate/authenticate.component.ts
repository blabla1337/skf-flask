import { Component } from '@angular/core';
import { AuthenticateService } from '../services/authenticate.service';

@Component({
  selector: 'app-authenticate',
  templateUrl: './authenticate.component.html',
  providers: [AuthenticateService]
})

export class AuthenticateComponent {
  public username: string;
  public password: string;
  public error: string[] = [];
  public return: boolean;

  constructor(public _authenticateService: AuthenticateService) { }

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
          sessionStorage.setItem("user", response["Authorization token"]);
          location.replace("dashboard");
        } else { this.error.push("Wrong username/password combination!"); }
      })
  }
}
