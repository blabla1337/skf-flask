import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PagetitleComponent } from './pagetitle/pagetitle.component';

@NgModule({
  declarations: [PagetitleComponent],
  imports: [
    CommonModule,
  ],
  exports: [PagetitleComponent]
})
export class UIModule { }
