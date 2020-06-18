import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { KnowledgeBaseRoutingModule } from './knowledgebase-routing.module';
import { ReadComponent } from './read/read.component'; 

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    KnowledgeBaseRoutingModule
  ]
})
export class KnowledgebaseModule { }
