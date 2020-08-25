import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { ArchwizardModule } from 'angular-archwizard';
import { UIModule } from '../shared/ui/ui.module';

// tslint:disable-next-line: import-spacing
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
import { LinksFilterPipe } from '../core/pipes/linksfilter.pipe';
import { HighlightModule, HIGHLIGHT_OPTIONS } from 'ngx-highlightjs';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgxSpinnerModule } from 'ngx-spinner';
import { JoyrideModule } from 'ngx-joyride';
import { CoreModule } from '../core/core.module';

import { AuthGuard } from '../core/guards/guard.service';
import { LoggedInAuthGuard } from '../core/guards/loggedinguard.service';

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
import { AddChecklistComponent } from './checklists/add-checklist/add-checklist.component';
import { UpdateChecklistComponent } from './checklists/update-checklist/update-checklist.component';
import { CreateCategoryComponent } from './category/create/create.component';
import { UpdateCategoryComponent } from './category/update/update.component';
import { IndexComponent } from './search/index/index.component';
import { CategoryManageComponent } from './category/manage/manage.component';
import { UpdateQuestionnaireComponent } from './checklists/questionnaire/update/update.component';
import { CreateQuestionnaireComponent } from './checklists/questionnaire/create/create.component';
import { UpdateChecklistTypeComponent } from './checklists/checklist-type/update/update.component';
import { CreateChecklistTypeComponent } from './checklists/checklist-type/create/create.component';
import { Page404Component } from './extra/page404/page404.component';
import { Page500Component } from './extra/page500/page500.component';

@NgModule({
  declarations: [
    ManageComponent, ViewCodeComponent, UpdateCodeComponent, CreateCodeComponent, ViewKnowledebaseComponent, CategoryManageComponent,
    ViewComponent, ProjectManageComponent, ProjectViewComponent, UserCreateComponent, AddChecklistComponent, UpdateQuestionnaireComponent,
    ChecklistsReadComponent, ChecklistCreateComponent, CheckManageComponent, WizardComponent, CreateCategoryComponent,
    LabReadComponent, LabViewComponent, SummaryComponent, UserUpdateComponent, UpdateChecklistComponent, UpdateCategoryComponent,
    CreateComponent, UpdateComponent, ProjectCreateComponent, ProjectUpdateComponent, StringFilterPipe, LabelFilterPipe,LinksFilterPipe,
    IndexComponent, CreateQuestionnaireComponent, UpdateChecklistTypeComponent, CreateChecklistTypeComponent, Page404Component, Page500Component
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
    NgxSpinnerModule,
    JoyrideModule.forChild(),
    CoreModule
  ],
  providers: [AuthGuard, LoggedInAuthGuard],
})
export class PagesModule { }
