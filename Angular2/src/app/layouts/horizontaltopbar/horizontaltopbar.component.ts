import { Component, OnInit, AfterViewInit, Inject } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { JoyrideService } from 'ngx-joyride';
import { ThemeService } from '../../core/services/theme.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DOCUMENT } from '@angular/common';
import { OAuthService } from 'angular-oauth2-oidc';

import { ChecklistCategoryService } from '../../core/services/checklist_category.service';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-horizontaltopbar',
  templateUrl: './horizontaltopbar.component.html',
  styleUrls: ['./horizontaltopbar.component.scss'],
  providers: [ThemeService]
})

/**
 * Horizontal Topbar and navbar specified
 */
export class HorizontaltopbarComponent implements OnInit, AfterViewInit
{

  public element;
  public configData;
  public theme: string;
  public dark = false;
  public light = true;
  public menuItems = [];
  public categoryData: any = [];
  public routeUrl: any;
  public themeName: string;
  public search: string;
  public searchForm: FormGroup;
  public priv: string = ""
  public logoutButton = environment.AUTH_METHOD;
  
  // tslint:disable-next-line: max-line-length
  constructor(
    @Inject(DOCUMENT) private document: any,
    private router: Router,
    // tslint:disable-next-line: variable-name
    private _checklistCategoryService: ChecklistCategoryService,
    private readonly joyride: JoyrideService,
    private themeService: ThemeService,
    private formBuilder: FormBuilder,
    private oauthService: OAuthService,
  ) {}

  

  ngOnInit(): void
  {
    let token = ""

    if (sessionStorage.getItem("access_token") !== null) {
      token = sessionStorage.getItem("access_token")
    }

    if(token == ""){
      localStorage.setItem("privilege", "manage")
    }

    if(environment.AUTH_METHOD == "openidprovider"){
      if(token == ""){
        window.location.assign("/auth/login");
      }
      if(token != ""){
        let decoded = atob(token.split('.')[1])
        if(decoded.match("admin")){
          localStorage.setItem("privilege", "manage");
        }
      }
    } 
    
    this.element = document.documentElement;

    this.searchForm = this.formBuilder.group({
      search: [''],
    });

    // this.initialize();

    this.configData = {
      suppressScrollX: true,
      wheelSpeed: 0.3
    };

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);

    this.themeName = localStorage.getItem('theme');
    this.changeTheme(this.themeName);
    if (this.themeName === 'dark-theme.css') {
      this.dark = true;
      this.light = false;
    } else {
      this.light = true;
      this.dark = false;
    }
  }

  ngAfterViewInit() {}

  /**
   * Togglemenu bar
   */
  toggleMenubar()
  {
    const element = document.getElementById('topnav-menu-content');
    element.classList.toggle('show');
  }

  /**
   * Change to Dark theme
   */
  toDark(theme: string)
  {
    document.getElementById('skf-logo-text-large').style.color = 'white' ; 
    document.getElementById('skf-logo-text-small').style.color = 'white' ; 
    this.themeService.editTheme(theme);
    this.dark = true;
    this.light = false;
    this.themeName = localStorage.getItem('theme');
    this.changeTheme(this.themeName);
  }

  /**
   * Change to Light theme
   */
  toLight(theme: string)
  {
    document.getElementById('skf-logo-text-large').style.color = '#8184B2' ; 
    document.getElementById('skf-logo-text-small').style.color = '#8184B2' ; 
    this.themeService.editTheme(theme);
    this.light = true;
    this.dark = false;
    this.themeName = localStorage.getItem('theme');
    this.changeTheme(this.themeName);
  }

  /**
   * Dynamic Theme
   */
  changeTheme(styleName: string)
  {
    const head = this.document.getElementsByTagName('head')[0];
    const themeLink = this.document.getElementById('dynamic-theme') as HTMLLinkElement;
    if (themeLink) {
      themeLink.href = styleName;
    } else {
      const style = this.document.createElement('link');
      style.id = 'dynamic-theme';
      style.rel = 'stylesheet';
      style.href = `${styleName}`;

      head.appendChild(style);
    }
  }

  /**
   * Tour
   */
  tour()
  {
    this.routeUrl = this.router.url;

    if(this.routeUrl == "/code-example/view"){
      this.joyride.startTour({
        steps: [
          'codeCat', 'codeAdd', 'codeRow',     // tour code examples page             
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl == "/knowledgebase/view"){
      this.joyride.startTour({
        steps: [
          'kbCat', 'kbAdd', 'kbRow', 'userActivated', 'userRole', 'userDisable', // tour user manage page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl == "/labs/view"){
      this.joyride.startTour({
        steps: [
          'nameLabContent', 'labelLabContent', 'levelLabContent', 'statusLabContent', 'writeLabContent', 'actionLabContent', // tour lab page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl.includes("/projects/view/")){
      this.joyride.startTour({
        steps: [
          'projectRequirements', 'projectRequirementsResults', // tour project view page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'top',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl == "/projects/manage"){
      this.joyride.startTour({
        steps: [
          'projectName', 'createProject', 'startProject', 'updateProject', // tour project manage page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl.includes("/projects/summary/")){
      this.joyride.startTour({
        steps: [
          'resultControl', 'resultControlKB',  // tour project summary page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl == "/users/manage"){
      this.joyride.startTour({
        steps: [
          'userNew', 'userName', 'userEmail', 'userActivated', 'userRole', 'userDisable', // tour user manage page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl == "/checklists/view"){
      this.joyride.startTour({
        steps: [
          'catChecklistContent', 'addChecklistContent', 'topicsChecklistContent', 'viewChecklistContent', 'manageChecklistContent', // tour checklist view page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }

    if(this.routeUrl.includes("/checklists/manage/")){
      this.joyride.startTour({
        steps: [
          'manageInfo', 'manageConfig', 'manageReq', 'manageQuestions',  // tour project checklist manage page
        ], 
        showPrevButton: true,
        stepDefaultPosition: 'bottom',
        themeColor: '#000',
        showCounter: false,
      });
    }
  }

  /**
   * Returns true or false if given menu item has child or not
   * @param item menuItem
   */
  
  platformUpdate(platform: string)
  {
    localStorage.setItem('categorySelector', platform);
    this.document.defaultView.location.reload();
  }

  loggedOut()
  {
    this.oauthService.logOut();
    localStorage.clear();
    sessionStorage.clear();
    this.router.navigate(['/auth/login']);
  }

  onChange() 
  {
    localStorage.setItem('search',this.searchForm.value.search)
    this.router.navigate(['/search/index']);
  }

  
  get form()
  {
    return this.searchForm.controls;
  }

}
