import { Component, OnInit } from '@angular/core';
import {HeaderComponent} from '../header/header.component';
import { Project } from '../models/project';
import { AppSettings } from '../globals';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html'
})

export class DashboardComponent implements OnInit {

  projects: Project[];
  constructor() { }

  public skipLogin: boolean;

  ngOnInit() {
  	if (AppSettings.SKIP_LOGIN == "true") {
      this.skipLogin = true;
  	}
  }

}
