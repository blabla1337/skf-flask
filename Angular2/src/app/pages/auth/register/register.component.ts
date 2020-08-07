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
      userId: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      accessToken: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      userName: ['', Validators.required],
      userEmail: ['', Validators.required],
      userPassword: ['', [Validators.required, Validators.minLength(8)]],
      confirmPassword: ['', Validators.required],
    }, { validators: this.passwordMatchingValidatior });
  }

  passwordMatchingValidatior(fg: FormGroup): Validators {
    return fg.get('userPassword').value === fg.get('confirmPassword').value ? null :
      { notmatched: true };
  }


  onSubmit() {
    console.log(this.registerationForm.value);
    this.userSubmitted = true;

    if (this.registerationForm.valid) {
      console.log("Woooooooooooop");
      // this.user = Object.assign(this.user, this.registerationForm.value);    this._projectService.createProject(this.projectForm.value).subscribe()

      this._userService.activateUser(this.userData(), this.userId.value).subscribe();
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
      userName: this.userName.value,
      accessToken: this.accessToken.value,
      userEmail: this.userEmail.value,
      userPassword: this.userPassword.value,
      confirmPassword: this.confirmPassword.value,
    }
  }

  // ------------------------------------
  // Getter methods for all form controls
  // ------------------------------------
  get userName() {
    return this.registerationForm.get('userName') as FormControl;
  }

  get userEmail() {
    return this.registerationForm.get('userEmail') as FormControl;
  }
  get userPassword() {
    return this.registerationForm.get('userPassword') as FormControl;
  }
  get confirmPassword() {
    return this.registerationForm.get('confirmPassword') as FormControl;
  }
  get userId() {
    return this.registerationForm.get('userId') as FormControl;
  }
  get accessToken() {
    return this.registerationForm.get('accessToken') as FormControl;
  }
  // --------------------

}
