import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ArchwizardModule } from 'angular-archwizard';
import { UIModule } from '../shared/ui/ui.module';

import
{
  NgbNavModule, NgbDropdownModule, NgbModalModule,
  NgbTooltipModule, NgbPaginationModule, NgbTypeaheadModule,
  NgbCollapseModule,
} from '@ng-bootstrap/ng-bootstrap';

import { PagesRoutingModule } from './pages-routing.module';
import { DashboardModule } from './dashboard/dashboard.module';
import { UsersModule } from './users/users.module';
import { DndModule } from 'ngx-drag-drop';
import { StringFilterPipe } from '../core/pipes/stringfilter.pipe';
import { LabelFilterPipe } from '../core/pipes/labelfilter.pipe';
import { HighlightModule, HIGHLIGHT_OPTIONS } from 'ngx-highlightjs';
import { NgSelectModule } from '@ng-select/ng-select';

// Import Components here
import { ManageComponent } from './users/manage/manage.component';
import { ViewCodeComponent } from './code-example/view/view.component';
import { UpdateCodeComponent } from './code-example/update/update.component';
import { CreateCodeComponent } from './code-example/create/create.component';
import { ViewKnowledebaseComponent } from './knowledgebase/view/view.component';
import { CreateComponent } from './knowledgebase/create/create.component';
import { UpdateComponent } from './knowledgebase/update/update.component';
import { ViewComponent } from './checklists/view/view.component';
import { ChecklistsReadComponent } from './checklists/read/read.component';
import { CheckManageComponent } from './checklists/manage/manage.component';
import { ProjectManageComponent } from './projects/manage/manage.component';
import { ProjectViewComponent } from './projects/view/view.component';
import { ProjectUpdateComponent } from './projects/update/update.component';
import { ProjectCreateComponent } from './projects/create/create.component';
import { LabReadComponent } from './labs/read/read.component';
import { LabViewComponent } from './labs/view/view.component';
import { SummaryComponent } from './projects/summary/summary.component';
import { WizardComponent } from './projects/wizard/wizard.component';
import { ChecklistCreateComponent } from './checklists/create/create.component';
import { UserCreateComponent } from './users/create/create.component';
import { UserUpdateComponent } from './users/update/update.component';
import { AddChecklistComponent } from './checklists/addchecklist/addchecklist.component';
import { UpdateChecklistComponent } from './checklists/updatechecklist/updatechecklist.component';
import { AddCategoryComponent } from './checklists/addcategory/addcategory.component';
import { UpdateCategoryComponent } from './checklists/updatecategory/updatecategory.component';

@NgModule({
  declarations: [
    ManageComponent, ViewCodeComponent, UpdateCodeComponent, CreateCodeComponent, ViewKnowledebaseComponent,
    ViewComponent, ProjectManageComponent, ProjectViewComponent, UserCreateComponent, AddChecklistComponent,
    ChecklistsReadComponent, ChecklistCreateComponent, CheckManageComponent, WizardComponent, AddCategoryComponent,
    LabReadComponent, LabViewComponent, SummaryComponent, UserUpdateComponent, UpdateChecklistComponent, UpdateCategoryComponent,
    CreateComponent, UpdateComponent, ProjectCreateComponent, ProjectUpdateComponent, StringFilterPipe, LabelFilterPipe
  ],
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
    ReactiveFormsModule,
    ArchwizardModule,
    UsersModule,
    UIModule,
    DndModule,
    HighlightModule,
    NgSelectModule,
  ],
  providers: [],
})
export class PagesModule { }
