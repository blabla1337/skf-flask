import { Component, OnInit, AfterViewChecked } from '@angular/core';
import { Router } from '@angular/router';
import { NgxSpinnerService } from 'ngx-spinner';

import { SearchService } from '../../../core/services/search.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})

export class IndexComponent implements OnInit, AfterViewChecked
{

  // bread crumb items
  public breadCrumbItems: Array<{}>;
    // Collapse value
  public isCollapsed: boolean[] = [];
  public results_checklist: any = [];
  public results_labs: any = [];
  public results_kb: any = [];
  public results_projects: any = [];
  public search: string;
  public check: boolean;
  public check_status: boolean = false;
  public lab_status: boolean = false;
  public kb_status: boolean = false;
  public pro_status: boolean = false;
  public length;

  constructor(
    private router: Router,
    private _searchService: SearchService,
    private spinner: NgxSpinnerService,
  ) { }

  ngOnInit(): void
  {
    this.breadCrumbItems = [{ label: 'Search' }, { label: 'Index', active: true }];
    this.getCheck();
    this.search = localStorage.getItem('search');
    this.length = this.results_checklist.length;
    console.log(this.length);
  }


  ngAfterViewChecked(): void
  {
    if (localStorage.getItem('search') != this.search) {
      this.search = localStorage.getItem('search');
      window.location.reload();
    }
  }


  getCheck()
  {
    this.check_status = true;
    this.lab_status = false;
    this.kb_status = false;
    this.pro_status = false;
    if (localStorage.getItem("search") !== "") {
      this.spinner.show();
      this._searchService.searchChecklist(localStorage.getItem("search")).subscribe(results =>
      {
        this.results_checklist = results;
        this.spinner.hide();
      });
    }
  }

  getKB()
  {
    this.lab_status = false;
    this.kb_status = true;
    this.pro_status = false;
    this.check_status = false;
    if (localStorage.getItem("search") !== "") {
      this.spinner.show();
      this._searchService.searchKb(localStorage.getItem("search")).subscribe(results =>
      {
        this.results_kb = results;
        this.spinner.hide();
      });
    }
  }

  getLab()
  {
    this.kb_status = false;
    this.pro_status = false;
    this.check_status = false;
    this.lab_status = true;
    if (localStorage.getItem("search") !== "") {
      this.spinner.show();
      this._searchService.searchLabs(localStorage.getItem("search")).subscribe(results =>
      {
        this.results_labs = results;
        console.log(this.results_labs)
        this.spinner.hide();
      });
    }
  }

  getProj()
  {
    this.pro_status = true;
    this.check_status = false;
    this.lab_status = false;
    this.kb_status = false;
    if (localStorage.getItem("search") !== "") {
      this.spinner.show();
      this._searchService.searchProject(localStorage.getItem("search")).subscribe(results =>
      {
        this.results_projects = results;
        this.spinner.hide();
      });
    }
  }

}
