import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HighlightModule, HIGHLIGHT_OPTIONS } from 'ngx-highlightjs';

import { CodeExampleRoutingModule } from './code-example-routing.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    CodeExampleRoutingModule,
    HighlightModule
  ]
})
export class CodeExampleModule { }
