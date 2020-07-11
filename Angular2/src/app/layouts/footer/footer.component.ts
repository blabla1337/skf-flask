import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-footer',
  templateUrl: './footer.component.html',
  styleUrls: ['./footer.component.scss']
})
export class FooterComponent implements OnInit {

  // set the currenr year
  year: number = new Date().getFullYear();
  
  constructor() { }

  ngOnInit(): void {
  }

}
