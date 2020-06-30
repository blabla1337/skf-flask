import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { FormBuilder, Validators, FormGroup } from '@angular/forms';
import { Match } from './validation.match';

import { Users } from './manage.model';

import { usersData } from './data';

@Component({
  selector: 'app-manage',
  templateUrl: './manage.component.html',
  styleUrls: ['./manage.component.scss']
})
export class ManageComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  usersData: Users[];

  // page
  currentpage: number;

  // Form Validation
  validationform: FormGroup;

  // Form Submission
  submit: boolean;
  formsubmit: boolean;
  Allow = false;

  constructor( private modalService: NgbModal,  private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.breadCrumbItems = [{ label: 'Users' }, { label: 'Details', active: true }];

    this.currentpage = 1;

    this.Allow = true;

    /**
     * Fetches the data
     */
    this._fetchData();

    /**
     * Bootstrap validation form data
     */
    this.validationform = this.formBuilder.group({
      firstName: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      lastName: ['', [Validators.required, Validators.pattern('[a-zA-Z0-9]+')]],
      email: ['', [Validators.required, Validators.pattern('[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$')]],
    });
    this.submit = false;
  }

  /**
   * Customers data fetches
   */
  private _fetchData() {
    this.usersData = usersData;
  }

  /**
   * Open center modal
   * @param centerDataModal center modal data
   */
  centerModal(centerDataModal: any) {
    this.modalService.open(centerDataModal, { centered: true });
  }

  /**
   * Returns form
   */
  get form() {
    return this.validationform.controls;
  }

  /**
   * Bootsrap validation form submit method
   */
  validSubmit() {
    this.submit = true;
  }

}
