import { Component } from '@angular/core';
import { Router } from '@angular/router'
import { User } from '../models/user'
import { AuthenticateService } from '../services/authenticate.service'
@Component({
  selector: 'app-first-login',
  templateUrl: './first-login.component.html',
  providers: [AuthenticateService]
})
export class FirstLoginComponent {

  constructor(private activate: AuthenticateService, private router: Router) { }

  public username: string;
  public password: string;
  public repassword: string;
  public accessToken: string;
  public userID: number;
  public email: string
  public user: User[] = []
  public error: string[] = [];
  public return: boolean;

  activateUser() {
    this.error = []
    this.return = true;
    if (!this.email) {this.return = false; this.error.push('Email field was left empty')}
    if (!this.password) {this.return = false; this.error.push('Password field was left empty')}
    if (!this.repassword) {this.return = false; this.error.push('Repassword field was left empty')}
    if (!this.accessToken) {this.return = false; this.error.push('AccessToken field was left empty')}
    if (!this.username) {this.return = false; this.error.push('Username field was left empty')}
    if (!this.userID) {this.return = false; this.error.push('UserID field was left empty')}

    if (this.return == false) {return; }

    this.activate.activateUser(this.email, this.username, this.accessToken, this.password, this.repassword, this.userID).subscribe(resp => {},
      err => this.error.push('User could not be activated, contact your administrator!' ),
      () => {this.router.navigate(['/login'])} )
  }
}
