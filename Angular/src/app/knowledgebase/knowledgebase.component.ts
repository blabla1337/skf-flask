import { Component, OnInit, ElementRef } from '@angular/core';
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { Knowledgebase } from '../models/knowledgebase';
import { StartsWithPipe } from '../pipes/starts-with.pipe'
import { ReplaySubject } from 'rxjs/Rx';

@Component({
  selector: 'app-knowledgebase',
  templateUrl: './knowledgebase.component.html'
})

export class KnowledgebaseComponent implements OnInit {
  
  public knowledgeitems: Knowledgebase[]
  public queryString: string;
  public error: string;
  constructor(public _knowledgeService: KnowledgebaseService) { }

  ngOnInit() {
    this.getKnowledgeItems();
  }

  getKnowledgeItems() {
    this._knowledgeService.getKnowledgeBase().subscribe(requestData => {
      this.knowledgeitems = requestData
      if (!this.knowledgeitems) {
        this.error = "Error getting knowledge items, contact the administrator!"
      }
    },
      err => this.error = "Error getting knowledge items, contact the administrator!"
    );
  }

}
