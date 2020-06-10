import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';


import { PagesRoutingModule } from './pages-routing.module';
import { DashboardModule } from './dashboard/dashboard.module';
import { ManageComponent } from './users/manage/manage.component';
import { NgbNavModule, NgbDropdownModule, NgbModalModule, NgbTooltipModule, NgbPaginationModule, NgbTypeaheadModule } from '@ng-bootstrap/ng-bootstrap';



@NgModule({
  declarations: [ManageComponent],
  imports: [
    CommonModule,
    DashboardModule,
    PagesRoutingModule,
    NgbPaginationModule,
    NgbNavModule,
    NgbDropdownModule,
    FormsModule,
  ],
  providers: []
})
export class PagesModule { }
