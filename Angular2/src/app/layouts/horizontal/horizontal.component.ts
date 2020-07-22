import { Component, OnInit, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-horizontal',
  templateUrl: './horizontal.component.html',
  styleUrls: ['./horizontal.component.scss']
})

/**
 * Horizontal-layout component
 */
export class HorizontalComponent implements OnInit, AfterViewInit {

  constructor() { }

  ngOnInit() {
    document.body.setAttribute('data-layout', 'horizontal');
    document.body.setAttribute('data-topbar', 'dark');
  }

  ngAfterViewInit() {
  }
}
