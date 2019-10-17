import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { AuthenticateService } from '../services/authenticate.service';

@Component({
  selector: 'app-authenticate',
  templateUrl: './authenticate.component.html',
  providers: [AuthenticateService]
})

export class AuthenticateComponent implements OnInit {
  public error: string[] = [];
  public expired = false;
  loginForm: FormGroup;
  get formControls() { return this.loginForm.controls; }

  constructor(public _authenticateService: AuthenticateService, private formBuilder: FormBuilder) { }

  ngOnInit() {
    if (localStorage.getItem('session') == 'expired') { this.expired = true }localStorage.clear();
    this.loginForm = this.formBuilder.group({
      userName: ['', Validators.required],
      password: ['', Validators.required],
    })
  }
    
  onLogin() {
    this.error = [];
    this._authenticateService.authenticate(this.loginForm.value).subscribe(
      response => {
        if (response['Authorization token'] != '') {
          sessionStorage.setItem('auth_token', response['Authorization token']);
          sessionStorage.setItem('user', response['userName']);
          location.replace('dashboard');
        } else { this.error.push('Wrong username/password combination!'); }
      })
  }

  skipLogin() {
    sessionStorage.setItem('skip_login', 'true');
    location.replace('dashboard');
  }
}
