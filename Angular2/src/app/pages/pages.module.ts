import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UIModule } from '../shared/ui/ui.module';

import { PagesRoutingModule } from './pages-routing.module';
import { DashboardModule } from './dashboard/dashboard.module';
import { ManageComponent } from './users/manage/manage.component';
import { CodeViewComponent } from './code-example/view/view.component';
import { ReadComponent } from './knowledgebase/read/read.component';
import { ViewComponent } from './checklists/view/view.component';
import { NgbNavModule, NgbDropdownModule, NgbModalModule, NgbTooltipModule, NgbPaginationModule, NgbTypeaheadModule, NgbCollapseModule } from '@ng-bootstrap/ng-bootstrap';



@NgModule({
  declarations: [ManageComponent, CodeViewComponent, ReadComponent, ViewComponent],
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
