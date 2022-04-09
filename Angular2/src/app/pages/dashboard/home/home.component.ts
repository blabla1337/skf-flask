import { Component, OnInit } from '@angular/core';
import { NgbModal } from '@ng-bootstrap/ng-bootstrap';
import { JoyrideService } from 'ngx-joyride';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit
{

  constructor(
    private readonly joyride: JoyrideService
  ) { }

  ngOnInit(): void
  {
    if(localStorage.getItem('theme') == "light-theme.css"){
    document.getElementById('skf-logo-text-large').style.color = '#8184B2' ; 
    document.getElementById('skf-logo-text-small').style.color = '#8184B2' ; 
    }
  }

  tour()
  {
    this.joyride.startTour({
      steps: ['styleInfo', 'tourInfo', 'checklistCat', 
              'dashContent', 'projectContent', 'codeContent',
              'checkContent', 'knowledgebaseContent', 'userContent', 
              'labContent', 'trainingContent'
            ],
      showPrevButton: true,
      stepDefaultPosition: 'bottom',
      themeColor: '#000',
      showCounter: false,
    });
  }
}
