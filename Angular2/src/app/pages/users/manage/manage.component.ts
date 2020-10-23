import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { NgxSpinnerService } from 'ngx-spinner';

import { UserService } from '../../../core/services/user.service';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class ManageComponent implements OnInit
{

  // bread crumb items
  breadCrumbItems: Array<{}>;
  public revoke: string;
  public grant: string;

  // Form Validation
  validationform: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;
  public Allow = false;
  public usersList: any = [];
  public queryString;
  public privilegeData: any = [];

  constructor(
    private modalService: NgbModal,
    private formBuilder: FormBuilder,
    private _userService: UserService,
    private spinner: NgxSpinnerService,
  ) { }

  ngOnInit()
  {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Details', active: true }];

    this._fetchData();

    /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.pattern('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$')]],
    });
    this.submit = false;
  }

  /**
   * Customers data fetches
   */
  private _fetchData() 
  {
    this.spinner.show();
    this.getPrivileges();
    this._userService.getUsers().subscribe(users =>
    {
      this.usersList = users;
      this.spinner.hide();
    });
  }


  centerModal(centerDataModal: any)
  {
    this.modalService.open(centerDataModal, { centered: true, size: 'lg' });
  }


  get form()
  {
    return this.validationform.controls;
  }


  reloadAfterSelect()
  {
    this._fetchData();
  }

  validSubmit()
  {
    this.submit = true;
  }

  accountUserGrant(user_id: number)
  {
    if (this.grant == 'GRANT') {
      this._userService.accessUser('{"active":"True"}', user_id).subscribe(x => { this._fetchData() });
    }
  }

  accountUserRevoke(user_id: number)
  {
    if (this.revoke == 'REVOKE') {
      this._userService.accessUser('{"active":"False"}', user_id).subscribe(x => this._fetchData());
    }
  }

  accountUserPrivilege(privilege: any, user_id: number)
  {
    this._userService.accessUser('{"privilege_id":' + privilege + '}', user_id).subscribe(x => this._fetchData());
  }


  getPrivileges()
  {
    this._userService.getPrivileges().subscribe(x => this.privilegeData = x);
  }
}
