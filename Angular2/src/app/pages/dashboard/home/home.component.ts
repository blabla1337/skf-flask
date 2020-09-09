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
  }

  tour()
  {
    this.joyride.startTour({
      steps: ['styleInfo', 'tourInfo', 'checklistCat', 
              'dashContent', 'projectContent', 'codeContent',
              'checkContent', 'knowledgebaseContent', 'userContent', 'labContent'
            ],
      showPrevButton: true,
      stepDefaultPosition: 'bottom',
      themeColor: '#000',
      showCounter: false,
    });
  }
}
