import { Component, OnInit } from '@angular/core';
import {HeaderComponent} from '../header/header.component';
import { Project } from '../models/project';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html'
})

export class DashboardComponent implements OnInit {

  projects: Project[];
  constructor() { }

  ngOnInit() {
  }

}
