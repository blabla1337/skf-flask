import { Component, OnInit, AfterViewInit, Inject } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';
import { JoyrideService } from 'ngx-joyride';
import { ThemeService } from '../../core/services/theme.service';

import { DOCUMENT } from '@angular/common';

import { MENU } from './menu';
import { MenuItem } from './menu.model';
import { ChecklistCategoryService } from '../../core/services/checklist_category.service';

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

  element;
  configData;
  theme: string;
  loggedinUser: string;
  loggedin = false;
  dark = false;
  light = true;
  menuItems = [];
  categoryData: any = [];
  routeUrl: any;
  themeName: string;

  // tslint:disable-next-line: max-line-length
  constructor(@Inject(DOCUMENT) private document: any,
              private router: Router,
              // tslint:disable-next-line: variable-name
              private _checklistCategoryService: ChecklistCategoryService,
              private readonly joyride: JoyrideService,
              private themeService: ThemeService)
  {
    router.events.subscribe(event =>
    {
      if (event instanceof NavigationEnd) {
        this.activateMenu();
      }
    });
  }

  ngOnInit(): void
  {
    this.element = document.documentElement;

    this.initialize();

    this.configData = {
      suppressScrollX: true,
      wheelSpeed: 0.3
    };

    this._checklistCategoryService
      .getChecklistCategoryCollection()
      .subscribe(data => this.categoryData = data);

    this.themeName = sessionStorage.getItem('theme');
    this.changeTheme(this.themeName);
    if (this.themeName === 'dark-theme.css') {
      this.dark = true;
      this.light = false;
    } else {
      this.light = true;
      this.dark = false;
    }
  }

  /**
   * On menu click
   */
  onMenuClick(event: any)
  {
    const nextEl = event.target.nextSibling;
    if (nextEl && !nextEl.classList.contains('show')) {
      const parentEl = event.target.parentNode;
      if (parentEl) { parentEl.classList.remove('show'); }

      nextEl.classList.add('show');
    } else if (nextEl) { nextEl.classList.remove('show'); }
    return false;
  }

  ngAfterViewInit()
  {
    this.activateMenu();
  }

  /**
   * remove active and mm-active class
   */
  _removeAllClass(className)
  {
    const els = document.getElementsByClassName(className);
    while (els[0]) {
      els[0].classList.remove(className);
    }
  }

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
    this.themeService.editTheme(theme);
    this.dark = true;
    this.light = false;
    this.themeName = sessionStorage.getItem('theme');
    this.changeTheme(this.themeName);
  }

  /**
   * Change to Light theme
   */
  toLight(theme: string)
  {
    this.themeService.editTheme(theme);
    this.light = true;
    this.dark = false;
    this.themeName = sessionStorage.getItem('theme');
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
    this.joyride.startTour({
      steps: ['firstStep@' + this.routeUrl, 'secondStep', 'thirdStep', 'forthStep'], // stepid@routeurl
      showPrevButton: true,
      stepDefaultPosition: 'top',
      themeColor: '#000',
      showCounter: false,
    });
  }

  /**
   * Activates the menu
   */
  private activateMenu()
  {

    const resetParent = (el: any) =>
    {
      const parent = el.parentElement;
      if (parent) {
        parent.classList.remove('active');
        const parent2 = parent.parentElement;
        this._removeAllClass('mm-active');
        this._removeAllClass('mm-show');
        if (parent2) {
          parent2.classList.remove('active');
          const parent3 = parent2.parentElement;
          if (parent3) {
            parent3.classList.remove('active');
            const parent4 = parent3.parentElement;
            if (parent4) {
              parent4.classList.remove('active');
              const parent5 = parent4.parentElement;
              if (parent5) {
                parent5.classList.remove('active');
              }
            }
          }
        }
      }
    };

    // activate menu item based on location
    const links = document.getElementsByClassName('side-nav-link-ref');
    let matchingMenuItem = null;
    // tslint:disable-next-line: prefer-for-of
    for (let i = 0; i < links.length; i++) {
      // reset menu
      resetParent(links[i]);
    }
    // tslint:disable-next-line: prefer-for-of
    for (let i = 0; i < links.length; i++) {
      // tslint:disable-next-line: no-string-literal
      if (location.pathname === links[i]['pathname']) {
        matchingMenuItem = links[i];
        break;
      }
    }

    if (matchingMenuItem) {
      const parent = matchingMenuItem.parentElement;
      /**
       * TODO: This is hard coded way of expading/activating parent menu dropdown and working till level 3.
       * We should come up with non hard coded approach
       */
      if (parent) {
        parent.classList.add('active');
        const parent2 = parent.parentElement;
        if (parent2) {
          parent2.classList.add('active');
          const parent3 = parent2.parentElement;
          if (parent3) {
            parent3.classList.add('active');
            const parent4 = parent3.parentElement;
            if (parent4) {
              parent4.classList.add('active');
              const parent5 = parent4.parentElement;
              if (parent5) {
                parent5.classList.add('active');
              }
            }
          }
        }
      }
    }
  }

 /**
  * Initialize
  */
  initialize(): void
  {
    this.menuItems = MENU;
  }

  /**
   * Returns true or false if given menu item has child or not
   * @param item menuItem
   */
  hasItems(item: MenuItem)
  {
    return item.subItems !== undefined ? item.subItems.length > 0 : false;
  }

  platformUpdate(platform: string)
  {
    localStorage.setItem('categorySelector', platform);
    this.document.defaultView.location.reload();

  }

  onLogin()
  {
    this.router.navigate(['/auth/login']);
  }

  loggedIn()
  {
    this.loggedinUser = sessionStorage.getItem('Authorization');
    this.loggedin = true;
    return this.loggedinUser;
  }

  loggedOut()
  {
    sessionStorage.removeItem('Authorization');
    this.router.navigate(['/auth/login']);
  }
}
