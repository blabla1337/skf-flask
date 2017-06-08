import { Component, OnInit,ElementRef } from '@angular/core';
import {KnowledgebaseService} from '../services/knowledgebase.service'
import { Knowledgebase } from '../models/knowledgebase';
import {StartsWithPipe} from '../pipes/starts-with.pipe'


import { HighlightJsService } from 'angular2-highlight-js'; //in live this would be the node_modules path

@Component({
  selector: 'app-knowledgebase',
  templateUrl: './knowledgebase.component.html',
  providers: [KnowledgebaseService, HighlightJsService ],
})

export class KnowledgebaseComponent implements OnInit {
  private knowledgeitems : Knowledgebase[]
  public queryString:string;
  public error:string;
  constructor(private _knowledgeService:KnowledgebaseService,private highlightJsService: HighlightJsService,private el: ElementRef) { }

  ngOnInit() {
   this._knowledgeService.getKnowledgeBase().subscribe(requestData => 
           {
             this.knowledgeitems = requestData
             if(!this.knowledgeitems){
                this.error = "Error getting knowledge items, contact the administrator!"
             }
          },
             err => this.error = "Error getting knowledge items, contact the administrator!"
     );
     
  }

    highlightByService(target: ElementRef) {
        this.highlightJsService.highlight(target);
    }
}
