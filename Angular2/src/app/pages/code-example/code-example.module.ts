import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UIModule } from '../../shared/ui/ui.module';

import { CodeExampleRoutingModule } from './code-example-routing.module';
import { NgSelectModule } from '@ng-select/ng-select';
import { Ng2SearchPipeModule } from 'ng2-search-filter';
import { EditComponent } from './edit/edit.component';
import { CodeCreateComponent } from './create/create.component';



@NgModule({
  declarations: [EditComponent, CodeCreateComponent],
  imports: [
    CommonModule,
    CodeExampleRoutingModule,
    Ng2SearchPipeModule,
    NgSelectModule,
    UIModule
  ]
})
export class CodeExampleModule { }
