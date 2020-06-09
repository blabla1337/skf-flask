import { Component, OnInit } from '@angular/core';
import { NgbModal} from '@ng-bootstrap/ng-bootstrap';

import { Card } from './home';
import { CardItem } from './home.model';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  cardItems = [];

  ngOnInit(): void {
  }

 initialize(): void {
  this.cardItems = Card;
}
}
