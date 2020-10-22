import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user-manage.service';
import { User } from '../models/user';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-user-manage',
  templateUrl: './user-manage.component.html',
  providers: [UserService]
})

export class UserManageComponent implements OnInit
{
  users: User[];
  closeResult: string;
  public number: number;
  public error: string;
  public revoke_str: string;
  public grant_str: string;

  constructor(private _userService: UserService, private modalService: NgbModal) { }

  ngOnInit()
  {
    this.userList();
  }

  userRevokeAccess(id: number)
  {
    if (this.revoke_str == 'REVOKE') {
      this._userService.revokeUser(id).subscribe(x =>
        // Get the new user list on delete
        this.userList())
    }
  }

  userGrantAccess(id: number)
  {
    if (this.grant_str == 'GRANT') {
      this._userService.grantUser(id).subscribe(x =>
        // Get the new user list on delete
        this.userList())
    }
  }

  userList()
  {
    this._userService
      .getUsers()
      .subscribe(
        users =>
        {
          this.users = users;
        },
        err => this.error = 'Getting the users failed, contact an administrator! ');
  }

  open(content)
  {
    this.modalService.open(content);
  }
}
