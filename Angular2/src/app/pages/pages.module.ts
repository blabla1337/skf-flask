import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UIModule } from '../shared/ui/ui.module';

import { PagesRoutingModule } from './pages-routing.module';
import { DashboardModule } from './dashboard/dashboard.module';
import { ManageComponent } from './users/manage/manage.component';
import { NgbNavModule, NgbDropdownModule, NgbModalModule, NgbTooltipModule, NgbPaginationModule, NgbTypeaheadModule, NgbCollapseModule } from '@ng-bootstrap/ng-bootstrap';
import { CodeExampleComponent } from './code-example/code-example.component';



@NgModule({
  declarations: [ManageComponent, CodeExampleComponent],
  imports: [
    CommonModule,
    DashboardModule,
    PagesRoutingModule,
    NgbPaginationModule,
    NgbNavModule,
    NgbDropdownModule,
    NgbModalModule,
    NgbCollapseModule,
    NgbTooltipModule,
    NgbTypeaheadModule,
    FormsModule,
    UIModule
  ],
  providers: []
})
export class PagesModule { }
