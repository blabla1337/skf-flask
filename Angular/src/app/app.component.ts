import { Component, OnInit } from '@angular/core';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { KnowledgebaseService } from './services/knowledgebase.service'
import { Knowledgebase } from './models/knowledgebase'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  providers: [HeaderComponent, FooterComponent, KnowledgebaseService],
})

export class AppComponent implements OnInit {
  constructor(private _knowledgeService: KnowledgebaseService) { }
  private knowledgeitems: Knowledgebase[]

  ngOnInit() {
    this._knowledgeService.getKnowledgeBase().subscribe(requestData => {
      this.knowledgeitems = requestData
    });

    setTimeout(() => {
      localStorage.setItem('session', 'expired');
      location.replace('login');
    }, 6600000);
    // 6600000 == total time API gives
  }
}
