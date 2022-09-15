import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { JoyrideService } from 'ngx-joyride';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent implements OnInit {
  accordionItems: any[];
  constructor(/* private readonly joyride: JoyrideService */) {}

  ngOnInit(): void {
    const priv_setting = localStorage.getItem('privilege');
    if (
      priv_setting === undefined ||
      priv_setting === '' ||
      priv_setting === null
    ) {
      localStorage.setItem('privilege', 'manage');
    }

    const theme_var = localStorage.getItem('theme');
    if (theme_var === undefined || theme_var === '' || theme_var === null) {
      localStorage.setItem('theme', 'light-theme.css');
    }

    const cat_var = localStorage.getItem('categorySelector');
    if (cat_var === undefined || cat_var === '' || cat_var === null) {
      localStorage.setItem('categorySelector', '1');
    }

    if (localStorage.getItem('theme') == 'light-theme.css') {
      document.getElementById('skf-logo-text-large').style.color = '#8184B2';
      document.getElementById('skf-logo-text-small').style.color = '#8184B2';
    }

    this.accordionItems = [
      {
        id: 'developer',
        title: 'Developer',
        description:
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
        routerLink: '/projects/manage',
        display: true,
      },
      {
        id: 'pentester',
        title: 'Pentester',
        description:
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
        routerLink: '/labs/view',
        display: false,
      },
      {
        id: 'training',
        title: 'Training Labs',
        description:
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
        routerLink: '/training/profiles',
        display: false,
      },
      {
        id: 'checklist',
        title: 'Customize Checklist',
        description:
          'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua',
        routerLink: '/checklists/view',
        display: false,
      },
    ];
  }

  expandItem(e: Event, currentItem: any) {
    e.preventDefault();
    this.accordionItems.forEach((item) => {
      item.display = false;
      currentItem.display = true;
    });
  }

  /* tour() */
  /* { */
  /*   this.joyride.startTour({ */
  /*     steps: ['styleInfo', 'tourInfo', 'checklistCat',  */
  /*             'dashContent', 'projectContent', 'codeContent', */
  /*             'checkContent', 'knowledgebaseContent', 'userContent',  */
  /*             'labContent', 'trainingContent' */
  /*           ], */
  /*     showPrevButton: true, */
  /*     stepDefaultPosition: 'bottom', */
  /*     themeColor: '#000', */
  /*     showCounter: false, */
  /*   }); */
  /* } */
}
