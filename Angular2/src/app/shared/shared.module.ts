import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { UIModule } from './ui/ui.module';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    UIModule,
    FormsModule,
    ReactiveFormsModule,
  ],
})

export class SharedModule { }
