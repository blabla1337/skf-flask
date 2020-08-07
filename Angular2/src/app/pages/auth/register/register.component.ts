import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators, FormBuilder } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { UserService } from '../../../core/services/user.service';
import { Auth } from '../../../core/models/auth.model';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {

  year: number = new Date().getFullYear();
  registerationForm: FormGroup;
  user: Auth;
  userSubmitted: boolean;
  successmsg = false;
  errormsg = false;

  constructor(
    private fb: FormBuilder,
    private _userService: UserService,
    private router: Router
  ){ }

  ngOnInit() {
    this.createRegisterationForm();
  }

  createRegisterationForm() {
    this.registerationForm = this.fb.group({
      user_id: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      accessToken: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      username: ['', Validators.required],
      email: ['', Validators.required],
      password: ['', [Validators.required, Validators.minLength(8)]],
      repassword: ['', Validators.required],
    }, { validators: this.passwordMatchingValidatior });
  }

  passwordMatchingValidatior(fg: FormGroup): Validators {
    return fg.get('password').value === fg.get('repassword').value ? null :
      { notmatched: true };
  }


  onSubmit() {
    console.log(this.registerationForm.value);
    this.userSubmitted = true;

    if (this.registerationForm.valid) {
      this._userService.activateUser(this.userData(), this.user_id.value).subscribe();
      this.onReset();
      this.successmsg = true;
      this.router.navigate(['/auth/login']);
    } else {
      this.errormsg = true;
    }
  }

  onReset() {
    this.userSubmitted = false;
    this.registerationForm.reset();
  }


  userData(): Auth {
    return this.user = {
      username: this.username.value,
      accessToken: Number(this.accessToken.value),
      email: this.email.value,
      password: this.password.value,
      repassword: this.repassword.value,
    }
  }

  // ------------------------------------
  // Getter methods for all form controls
  // ------------------------------------
  get username() {
    return this.registerationForm.get('username') as FormControl;
  }
  get email() {
    return this.registerationForm.get('email') as FormControl;
  }
  get password() {
    return this.registerationForm.get('password') as FormControl;
  }
  get repassword() {
    return this.registerationForm.get('repassword') as FormControl;
  }
  get user_id() {
    return this.registerationForm.get('user_id') as FormControl;
  }
  get accessToken() {
    return this.registerationForm.get('accessToken') as FormControl;
  }
  // --------------------

}
