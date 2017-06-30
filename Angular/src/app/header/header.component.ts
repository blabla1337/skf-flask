import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppSettings } from '../globals';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
})

export class HeaderComponent implements OnInit {

  constructor(public router: Router) { }

  public isLoggedin: boolean;
  public projects: boolean;
  public users: boolean;
  public groups: boolean;
  public results: boolean;
  public code: boolean;
  public knowledge: boolean;
  public check: boolean;
  public user: string = AppSettings.USER;

  ngOnInit() {
    if (AppSettings.AUTH_TOKEN) {
      this.isLoggedin = true;
    }

    this.projects = false;
    this.users = false;
    this.groups = false;
    this.results = false;
    this.knowledge = false;
    this.check = false;
    this.code = false;


  }

  ProjectsShow() {
    this.projects = true;
    this.users = false;
    this.groups = false;
    this.results = false;
    this.knowledge = false;
    this.check = false;
    this.code = false;

  }

  UsersShow() {
    this.projects = false;
    this.users = true;
    this.groups = false;
    this.results = false;
    this.knowledge = false;
    this.check = false;
    this.code = false;
  }

  GroupsShow() {
    this.projects = false;
    this.users = false;
    this.groups = true;
    this.results = false;
    this.knowledge = false;
    this.check = false;
    this.code = false;
  }

  ResultsShow() {
    this.projects = false;
    this.users = false;
    this.groups = false;
    this.results = true;
    this.knowledge = false;
    this.check = false;
    this.code = false;
  }

  CodeShow() {
    this.projects = false;
    this.users = false;
    this.groups = false;
    this.results = false;
    this.knowledge = false;
    this.check = false;
    this.code = true;
  }

  KnowledgeShow() {
    this.projects = false;
    this.users = false;
    this.groups = false;
    this.results = false;
    this.knowledge = true;
    this.check = false;
    this.code = false;
  }

  CheckShow() {
    this.projects = false;
    this.users = false;
    this.groups = false;
    this.results = false;
    this.knowledge = false;
    this.check = true;
    this.code = false;
  }
  ResetAll() {
    this.projects = false;
    this.users = false;
    this.groups = false;
    this.results = false;
  }

  LogOff() {
    sessionStorage.removeItem('auth_token');
    location.reload();
  }

  selectLang(codeLang: string) {
    localStorage.setItem("code_lang", codeLang);
    this.router.navigate(['code-examples'])
  }

  

  getProjectStyle() { if (this.projects) { return "#515594"; } else { return "" } }
  getUSerStyle() { if (this.users) { return "#515594"; } else { return "" } }
  getGroupStyle() { if (this.groups) { return "#515594"; } else { return "" } }
  getKnowledgeStyle() { if (this.knowledge) { return "#515594"; } else { return "" } }
  getCodeStyle() { if (this.code) { return "#515594"; } else { return "" } }
  getChecklistStyle() { if (this.check) { return "#515594"; } else { return "" } }
  
}
