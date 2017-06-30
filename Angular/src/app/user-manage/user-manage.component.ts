import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user-manage.service';
import { User } from '../models/user';
import { NgbModal, ModalDismissReasons } from '@ng-bootstrap/ng-bootstrap';
import { Observable } from 'rxjs/Rx';

@Component({
  selector: 'app-user-manage',
  templateUrl: './user-manage.component.html',
  providers: [UserService]
})

export class UserManageComponent implements OnInit {
  users: User[];
  closeResult: string;
  public number: number;
  public error: string;
  public revoke_str: string;
  public grant_str: string;

  constructor(private _userService: UserService, private modalService: NgbModal) { }

  ngOnInit() {
    this.userList();
  }

  revoke(id: number) {
    if (this.revoke_str == "REVOKE") {
      this._userService.revoke(id).subscribe(x =>
        //Get the new user list on delete 
        this.userList())
    }
  }

  grant(id: number) {
    if (this.revoke_str == "GRANT") {
      this._userService.grant(id).subscribe(x =>
        //Get the new user list on delete 
        this.userList())
    }
  }

  userList() {
    this._userService
      .getUsers()
      .subscribe(
      users => {
        this.users = users;
        if (!this.users) {
          this.error = "There are no users to show!"
        }
      },
      err => this.error = "Getting the users failed, contact an administrator! ");
  }

  open(content) {
    this.modalService.open(content).result.then((result) => {
      this.closeResult = 'Closed with: ${result}';
    }, (reason) => {
      this.closeResult = 'Dismissed ${this.getDismissReason(reason)}';
    });
  }

  private getDismissReason(reason: any): string {
    if (reason === ModalDismissReasons.ESC) {
      return 'by pressing ESC';
    } else if (reason === ModalDismissReasons.BACKDROP_CLICK) {
      return 'by clicking on a backdrop';
    } else {
      return `with: ${reason}`;
    }
  }

}
