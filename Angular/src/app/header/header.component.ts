import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

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
  public color:string = '#515594';
  public user: string = AppSettings.USER;
  public canManage: boolean;
  public canEdit: boolean;
  public skipLogin: boolean;
  //public canDelete: boolean;
  //public canRead: boolean;

  ngOnInit() {
    if (AppSettings.AUTH_TOKEN) {
      this.isLoggedin = true;
      let decodedJWT = JWT(AppSettings.AUTH_TOKEN);
      this.canManage = decodedJWT.privilege.includes("manage");
      this.canEdit = decodedJWT.privilege.includes("edit");
    }

    console.log("skip login"+AppSettings.SKIP_LOGIN);
    if (AppSettings.SKIP_LOGIN == "true") {
       console.log("skip login is set to true");
       this.skipLogin = true 
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
    localStorage.clear();
    location.reload();
  }

  logIn() {
    sessionStorage.removeItem('skip_login');
    localStorage.clear();
    location.reload();
  }

  selectLang(codeLang: string) {
    localStorage.setItem("code_lang", codeLang);
    this.router.navigate(['code-examples'])
  }

  

  getProjectStyle() { if (this.projects) { return this.color; } else { return "" } }
  getUSerStyle() { if (this.users) { return this.color; } else { return "" } }
  getGroupStyle() { if (this.groups) { return this.color; } else { return "" } }
  getKnowledgeStyle() { if (this.knowledge) { return this.color; } else { return "" } }
  getCodeStyle() { if (this.code) { return this.color; } else { return "" } }
  getChecklistStyle() { if (this.check) { return this.color; } else { return "" } }
  
}
