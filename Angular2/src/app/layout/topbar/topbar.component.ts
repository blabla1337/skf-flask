import { Component, OnInit } from '@angular/core';

import { MENU } from './menu';
import { MenuItem } from './menu.model';

@Component({
  selector: 'app-topbar',
  templateUrl: './topbar.component.html',
  styleUrls: ['./topbar.component.scss']
})
export class TopbarComponent implements OnInit {
  menuItems = [];
  element;
  configData;
  ngOnInit(): void {
    this.element = document.documentElement;

    this.initialize();

    this.configData = {
      suppressScrollX: true,
      wheelSpeed: 0.3
    };
  }

  onMenuClick(event: any) {
    const nextEl = event.target.nextSibling;
    if (nextEl && !nextEl.classList.contains('show')) {
      const parentEl = event.target.parentNode;
      if (parentEl) { parentEl.classList.remove('show'); }

      nextEl.classList.add('show');
    } else if (nextEl) { nextEl.classList.remove('show'); }
    return false;
  }

  initialize(): void {
    this.menuItems = MENU;
  }

  toggleMenubar() {
    const element = document.getElementById('topnav-menu-content');
    element.classList.toggle('show');
  }
  /**
   * Returns true or false if given menu item has child or not
   * @param item menuItem
   */
  hasItems(item: MenuItem) {
    return item.subItems !== undefined ? item.subItems.length > 0 : false;
  }

}
