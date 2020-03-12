import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { UserAddService } from '../services/user-add.service'
import { User } from '../models/user'
import { Router } from '@angular/router'
import { Privilege } from '../models/privilege'


@Component({
  selector: 'app-user-add',
  templateUrl: './user-add.component.html',
  providers: [UserAddService]
})

export class UserAddComponent
{ // implements OnInit {

  public isSubmitted: boolean;
  public data: User[];
  public error: string[] = [];
  public privileges: Privilege[];
  userForm: FormGroup;
  get formControls() { return this.userForm.controls; }

  constructor(private _userAddService: UserAddService, private _router: Router, private formBuilder: FormBuilder) { }

  ngOnInit()
  {
    this.userForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      privilege_id: ['', Validators.required],
    })
    this.getPrivileges();
  }

  storeUser()
  {
    this.isSubmitted = true;
    if (this.userForm.invalid) {
      return;
    }
    this._userAddService.newUser(this.userForm.value)
      .subscribe(
        data => this.data = data,
        () => console.log("There is an error storing a user, potential duplicate email")
      );
  }

  getPrivileges()
  {
    this._userAddService.getPrivileges().subscribe(
      privileges => this.privileges = privileges,
      () => console.log('Getting privileges failed')
    )
  }
}
