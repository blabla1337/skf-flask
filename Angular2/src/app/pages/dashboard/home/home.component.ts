import { Component, OnInit } from '@angular/core';
import { NgbModal} from '@ng-bootstrap/ng-bootstrap';
import { JoyrideService } from 'ngx-joyride';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  //cardItems = [];
  title = 'Sample';

  constructor(
    private readonly joyride: JoyrideService
    ) { }

  ngOnInit(): void {
  }

  tour()
  {
    this.joyride.startTour({
      steps: ['firstStep', 'menuOne', 'menuTwo', 'menuThree', 'menuFour',
      'menuFive', 'menuSix', 'menuSeven', 'secondStep', 'thirdStep', 'forthStep'],
      showPrevButton: true,
      stepDefaultPosition: 'top',
      themeColor: '#000',
      showCounter: false,
    });
  }

}
