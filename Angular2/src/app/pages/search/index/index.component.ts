import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  styleUrls: ['./index.component.scss']
})
export class IndexComponent implements OnInit {

  // bread crumb items
  breadCrumbItems: Array<{}>;

  public routerURL;

  constructor(private router: Router) { }

  ngOnInit(): void {
    this.breadCrumbItems = [{ label: 'Search' }, { label: 'Index', active: true }];

    this.routerURL = this.router.url;
  }

}
