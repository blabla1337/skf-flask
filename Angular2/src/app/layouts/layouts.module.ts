import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { NgxSpinnerModule } from 'ngx-spinner';
import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';
import { JoyrideModule } from 'ngx-joyride';

import { LayoutComponent } from './layout.component';
import { HorizontalComponent } from './horizontal/horizontal.component';
import { HorizontaltopbarComponent } from './horizontaltopbar/horizontaltopbar.component';
import { FooterComponent } from './footer/footer.component';
import { LoaderComponent } from './loader/loader.component';

@NgModule({
  // tslint:disable-next-line: max-line-length
  declarations: [LayoutComponent, HorizontalComponent, HorizontaltopbarComponent, FooterComponent, LoaderComponent],
  imports: [
    CommonModule,
    RouterModule,
    NgbDropdownModule,
    NgxSpinnerModule,
    JoyrideModule.forRoot(),
    BrowserModule,
    FormsModule,
    ReactiveFormsModule
  ],
})
export class LayoutsModule { }
