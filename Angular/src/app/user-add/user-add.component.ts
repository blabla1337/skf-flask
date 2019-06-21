import { Component } from '@angular/core';
import { UserAddService } from '../services/user-add.service'
import { User } from '../models/user'
import { Router } from '@angular/router'
import { Privilege } from '../models/privilege'

@Component({
  selector: 'app-user-add',
  templateUrl: './user-add.component.html',
  providers: [UserAddService]
})

export class UserAddComponent { // implements OnInit {
  public email: string;
  public privilegeSelected: string;
  public return: boolean;
  public error: string[] = [];
  public data: User[];
  public privileges: Privilege[];
  constructor(private _userAddService: UserAddService, private _router: Router) { }

  ngOnInit() {
    this._userAddService.getPrivileges().subscribe(
      privileges => this.privileges = privileges,
      err => console.log('Getting privileges failed')
    )
  }

  save() {
    this.return = true;
    this.error = [];
    if (!this.email) { this.error.push('No email was provided!'); this.return = false; }
    const EMAIL_REGEXP = /^[a-z0-9!#$%&'*+\/=?^_`{|}~.-]+@[a-z0-9]([a-z0-9-]*[a-z0-9])?(\.[a-z0-9]([a-z0-9-]*[a-z0-9])?)*$/i;
    if (EMAIL_REGEXP.test(this.email) == false) { this.error.push('Email validation failed, provide a valid adress!');  this.return = false}
    if (!this.privilegeSelected) { this.error.push('No privilege was provided!'); this.return = false; }
    if (this.return == false) { return; }

    this._userAddService.newUser(this.email, this.privilegeSelected)
      .subscribe(
      data => this.data = data,
      err => this.error.push('Error whilst adding user, potential duplicate email adres!')
      );
      this.email = '';
  }
}
