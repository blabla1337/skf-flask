import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { UserService } from '../../../core/services/user.service';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.scss']
})
export class UserCreateComponent implements OnInit 
{

  // bread crumb items
  breadCrumbItems: Array<{}>;

  // Form Validation
  public userForm: FormGroup;

  // Form Submission
  public submit: boolean;
  public formsubmit: boolean;

  constructor( 
    private formBuilder: FormBuilder,
    private _userService: UserService,
  ) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Create', active: true }];

    /**
     * Bootstrap validation form data
     */
    this.userForm = this.formBuilder.group({
      privilege_id:['', [Validators.required]],
      email: ['', [Validators.required, Validators.pattern('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$')]],
    });
    this.submit = false;
  }

  newUser()
  {
    this.submit = true;
    if (this.userForm.invalid) {
      return;
    }
    this._userService.createUser(this.userForm.value).subscribe()
    //this.router.navigate(['/projects/manage'])
  }

  /**
   * Returns form
   */
  get form() {
    return this.userForm.controls;
  }

  /**
   * Validation form submit method
   */
  validSubmit() {
    this.submit = true;
  }

}
