import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UIModule } from '../../shared/ui/ui.module';

import { CodeExampleRouting } from './code-exampe-routing.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    CodeExampleRouting,
    UIModule
  ]
})
export class CodeExampleModule { }
