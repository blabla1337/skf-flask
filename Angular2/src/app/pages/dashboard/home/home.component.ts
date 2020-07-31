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

  constructor(private joyride: JoyrideService) { }

  ngOnInit(): void {
    console.log(localStorage.getItem('platformId'));
    this.tour();
  }

  tour() {
    this.joyride.startTour(
      {steps: ['firstStep']}
    );
  }

 initialize(): void {
  this.cardItems = Card;
}
}
