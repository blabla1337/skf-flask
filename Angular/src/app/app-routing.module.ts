import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ProjectDashboardComponent } from './project-dashboard/project-dashboard.component';
import { ProjectSummaryComponent } from './project-summary/project-summary.component';
import { PluginManagerComponent }   from './plugin-manager/plugin-manager.component';
import { UserAddComponent } from './user-add/user-add.component';
import { LabsComponent } from './labs/labs.component';
import { KnowledgebaseComponent } from './knowledgebase/knowledgebase.component';
import { KnowledgebaseEditComponent } from './knowledgebase-edit/knowledgebase-edit.component';
import { CodeExamplesComponent } from './code-examples/code-examples.component';
import { CodeExamplesEditComponent } from './code-examples-edit/code-examples-edit.component';
import { ChecklistComponent } from './checklist/checklist.component';
import { ChecklistManageComponent } from './checklist-manage/checklist-manage.component';
import { ChecklistEditComponent } from './checklist-edit/checklist-edit.component';
import { ChecklistAddNewComponent } from './checklist-add-new/checklist-add-new.component';
import { ChecklistSummaryComponent } from './checklist-summary/checklist-summary.component';
import { FirstLoginComponent } from './first-login/first-login.component';
import { AuthenticateComponent } from './authenticate/authenticate.component';
import { GuardService } from './guard/guard.service';
import { UserManageComponent } from './user-manage/user-manage.component';
import { UndefinedComponent } from './undefined/undefined.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';



export const appRoutes: Routes = [

  { path: 'dashboard', component: DashboardComponent, canActivate: [GuardService] },
  { path: 'labs', component: LabsComponent, canActivate: [GuardService] },
  { path: 'project-list', component: ProjectListComponent, canActivate: [GuardService] },
  { path: 'project-dashboard/:id', component: ProjectDashboardComponent, canActivate: [GuardService] },
  { path: 'plugin-manager', component: PluginManagerComponent, canActivate: [GuardService] },
  { path: 'undefined', component: UndefinedComponent, canActivate: [GuardService] },
  { path: 'project-summary/:id', component: ProjectSummaryComponent, canActivate: [GuardService] },
   { path: 'knowledgebase', component: KnowledgebaseComponent, canActivate: [GuardService] },
  { path: 'knowledgebase-edit/:id', component: KnowledgebaseEditComponent, canActivate: [GuardService] },
  { path: 'code-examples', component: CodeExamplesComponent, canActivate: [GuardService] },
  { path: 'code-examples-edit/:id', component: CodeExamplesEditComponent, canActivate: [GuardService] },
  { path: 'user-add', component: UserAddComponent, canActivate: [GuardService] },
  { path: 'user-manage', component: UserManageComponent, canActivate: [GuardService] },
  { path: 'checklist', component: ChecklistComponent, canActivate: [GuardService] },
  { path: 'checklist-manage/:id', component: ChecklistManageComponent, canActivate: [GuardService] },
  { path: 'checklist-edit/:id', component: ChecklistEditComponent, canActivate: [GuardService] },
  { path: 'checklist-add-new/:id', component: ChecklistAddNewComponent, canActivate: [GuardService] },
  { path: 'checklist-summary', component: ChecklistSummaryComponent, canActivate: [GuardService] },
  { path: 'login', component: AuthenticateComponent },
  { path: 'first-login', component: FirstLoginComponent },
  { path: 'questionnaire-sprint/:id', component: QuestionnaireComponent, canActivate: [GuardService] },
  { path: '**', component: DashboardComponent, canActivate: [GuardService] }
];
@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
