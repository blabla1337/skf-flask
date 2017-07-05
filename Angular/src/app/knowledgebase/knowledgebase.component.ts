import { Component, OnInit,ElementRef } from '@angular/core';
import {KnowledgebaseService} from '../services/knowledgebase.service'
import { Knowledgebase } from '../models/knowledgebase';
import {StartsWithPipe} from '../pipes/starts-with.pipe'

@Component({
  selector: 'app-knowledgebase',
  templateUrl: './knowledgebase.component.html',
  providers: [KnowledgebaseService],
})

export class KnowledgebaseComponent implements OnInit {
  private knowledgeitems : Knowledgebase[]
  public queryString:string;
  public error:string;

  constructor(private _knowledgeService:KnowledgebaseService) { }

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
}
