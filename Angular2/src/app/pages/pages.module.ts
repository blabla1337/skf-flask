import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PagesRoutingModule } from './pages-routing.module';
import { DashboardModule } from './dashboard/dashboard.module';


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    DashboardModule,
    PagesRoutingModule
  ],
  providers: []
})
export class PagesModule { }
