import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';

import { SearchService } from '../../../core/services/search.service';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;
  results_checklist: any = [];
  public routerURL;
  constructor(
    private router: Router,
    private _searchService: SearchService,
    private spinner: NgxSpinnerService, 
  ) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Search' }, { label: 'Index', active: true }];
    this.routerURL = this.router.url;
  }

    /**
   * Customers data fetches
   */
  private _fetchData() 
  {
    this.spinner.show();
    this._searchService.searchChecklist(localStorage.getItem("search")).subscribe(users => {
      //this.usersList = users;
      this.spinner.hide();
    });
  }
}
