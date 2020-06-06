import { Component, OnInit, AfterViewInit } from '@angular/core';

import {
  LAYOUT_HORIZONTAL
} from './layouts.model';

@Component({
  selector: 'app-layout',
  templateUrl: './layout.component.html',
  styleUrls: ['./layout.component.scss']
})
export class LayoutComponent implements OnInit, AfterViewInit {

  // layout related config
  layoutType: string;
  ngOnInit() {
    // default settings
    this.layoutType = LAYOUT_HORIZONTAL;
  }
  ngAfterViewInit() {
  }
}
