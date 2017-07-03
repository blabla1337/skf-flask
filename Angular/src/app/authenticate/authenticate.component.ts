import { Component, OnInit } from '@angular/core';
import { AuthenticateService } from '../services/authenticate.service';

@Component({
  selector: 'app-authenticate',
  templateUrl: './authenticate.component.html',
  providers: [AuthenticateService]
})

export class AuthenticateComponent implements OnInit {
  public username: string;
  public user: string;
  public password: string;
  public error: string[] = [];
  public return: boolean;
  public loggedin: string;
 
  constructor(public _authenticateService: AuthenticateService) { }

  ngOnInit(){
    this.loggedin= "";
  }
  
  onLogin() {
    this.return = true;
    this.error = [];
    
    if (!this.username) { this.return = false; this.error.push("No username was provided"); }
    if (!this.password) { this.return = false; this.error.push("No password was provided"); }
    if (this.return == false) { return; }

    this._authenticateService.authenticate(this.username, this.password).subscribe(
      response => {
        this.loggedin = response["Authorization token"];
        this.user = response["username"]
      })

    if (this.loggedin != "") {
      sessionStorage.setItem("auth_token", this.loggedin);
      sessionStorage.setItem("user", this.user);
      location.replace("dashboard");
    } else { this.error.push("Wrong username/password combination!"); }
  }
}
