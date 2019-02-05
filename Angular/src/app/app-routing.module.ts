import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ProjectNewComponent } from './project-new/project-new.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ProjectDashboardComponent } from './project-dashboard/project-dashboard.component';
import { ProjectSummaryComponent } from './project-summary/project-summary.component';
import { ProjectSummaryAuditComponent } from './project-summary-audit/project-summary-audit.component';
import { UserAddComponent } from './user-add/user-add.component';
import { KnowledgebaseComponent } from './knowledgebase/knowledgebase.component';
import { CodeExamplesComponent } from './code-examples/code-examples.component';
import { ChecklistComponent } from './checklist/checklist.component';
import { FirstLoginComponent } from './first-login/first-login.component';
import { AuthenticateComponent } from './authenticate/authenticate.component';

import { GuardService } from './guard/guard.service';
import { UserManageComponent } from "./user-manage/user-manage.component";
import { UndefinedComponent } from "./undefined/undefined.component";

export const appRoutes: Routes = [
  
  { path: 'dashboard', component: DashboardComponent, canActivate: [GuardService] },
  { path: 'project-new', component: ProjectNewComponent, canActivate: [GuardService] },
  { path: 'project-list', component: ProjectListComponent, canActivate: [GuardService] },
  { path: 'project-dashboard/:id', component: ProjectDashboardComponent, canActivate: [GuardService] },
  { path: 'undefined', component: UndefinedComponent, canActivate: [GuardService] },
  { path: 'project-summary/:id', component: ProjectSummaryComponent, canActivate: [GuardService] },
  { path: 'project-summary-audit/:id', component: ProjectSummaryAuditComponent, canActivate: [GuardService] },
  { path: 'knowledgebase', component: KnowledgebaseComponent, canActivate: [GuardService] },
  { path: 'code-examples', component: CodeExamplesComponent, canActivate: [GuardService] },
  { path: 'user-add', component: UserAddComponent, canActivate: [GuardService] },
  { path: 'user-manage', component: UserManageComponent, canActivate: [GuardService] },
  { path: 'checklist', component: ChecklistComponent, canActivate: [GuardService] },
  { path: 'login', component: AuthenticateComponent },
  { path: 'first-login', component: FirstLoginComponent },
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