import { Component, OnInit } from '@angular/core';
import { KnowledgebaseService } from '../services/knowledgebase.service'
import { FormBuilder, FormGroup, Validators } from  '@angular/forms';

@Component({
  selector: 'app-plugin-manager',
  templateUrl: './plugin-manager.component.html',
  providers: [KnowledgebaseService]
})

export class PluginManagerComponent implements OnInit {
  knowledgebaseForm: FormGroup;
  public isSubmitted: boolean;
  public delete: string;
  public queryString: string;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit() {
  }

  storeKnowledgebaseItem() {
    this.isSubmitted = true;
    if(this.knowledgebaseForm.invalid){
      return;
    }    
  }
}
