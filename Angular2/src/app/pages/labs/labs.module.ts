import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { LabsRoutingModule } from './lab-routing.module';
import { ReadComponent } from './read/read.component';

@NgModule({
  declarations: [ReadComponent],
  imports: [
    CommonModule,
    LabsRoutingModule,
  ]
})
export class LabsModule { }
