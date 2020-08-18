import { Component, OnInit } from '@angular/core';
import { NgbModal} from '@ng-bootstrap/ng-bootstrap';
import { JoyrideService } from 'ngx-joyride';

import { Card } from './home';
import { CardItem } from './home.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  cardItems = [];
  title = 'Sample';

  constructor(
    private readonly joyride: JoyrideService
    ) { }

  ngOnInit(): void {
    console.log(localStorage.getItem('platformId'));
  }

  tour()
  {
    this.joyride.startTour({
      steps: ['firstStep', 'secondStep', 'thirdStep', 'lastStep'],
      showPrevButton: true,
      stepDefaultPosition: 'top',
      themeColor: '#000',
      showCounter: false,
    });
  }

  initialize(): void {
    this.cardItems = Card;
  }
}
