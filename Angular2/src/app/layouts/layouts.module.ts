import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';


import { NgbDropdownModule } from '@ng-bootstrap/ng-bootstrap';

import { LayoutComponent } from './layout.component';
import { HorizontalComponent } from './horizontal/horizontal.component';
import { HorizontaltopbarComponent } from './horizontaltopbar/horizontaltopbar.component';
import { FooterComponent } from './footer/footer.component';

@NgModule({
  // tslint:disable-next-line: max-line-length
  declarations: [LayoutComponent, HorizontalComponent, HorizontaltopbarComponent, FooterComponent],
  imports: [
    CommonModule,
    RouterModule,
    NgbDropdownModule,
  ],
})
export class LayoutsModule { }
