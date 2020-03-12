import { Component, OnInit} from '@angular/core';
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';
import { Router } from '@angular/router'
import { AuthenticateService } from '../services/authenticate.service'

@Component({
  selector: 'app-first-login',
  templateUrl: './first-login.component.html',
  providers: [AuthenticateService]
})
export class FirstLoginComponent implements OnInit{
  activateForm: FormGroup;
  public isSubmitted: boolean;
  public error: string[] = [];
  
  get formControls() { return this.activateForm.controls; }

  constructor(private activate: AuthenticateService, private router: Router, private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.activateForm = this.formBuilder.group({
      user_id: ['', Validators.required],
      accessToken: ['', Validators.required],
      email: ['', Validators.required],
      username: ['', Validators.required],
      password: ['', Validators.required],
      repassword: ['', Validators.required],
    })
  }

  activateUser() {
    this.isSubmitted = true;
    if(this.activateForm.invalid){
      return;
    }
    this.activate.activateUser(this.activateForm.value).subscribe(resp => {},
      () => console.log('User could not be activated, contact your administrator!' ),
      () => {this.router.navigate(['/login'])} )
  }
}
