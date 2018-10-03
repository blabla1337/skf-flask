/*
Dependencies:
https://ng-bootstrap.github.io/#/getting-started
npm install --save @ng-bootstrap/ng-bootstrap
npm install --save angular2-highlight-js

*/

import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { AppRoutingModule } from './app-routing.module';
import { ProjectNewComponent } from './project-new/project-new.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ProjectDashboardComponent }   from './project-dashboard/project-dashboard.component';
import { ProjectSummaryComponent }   from './project-summary/project-summary.component';
import { ProjectSummaryAuditComponent }   from './project-summary-audit/project-summary-audit.component';
import { KnowledgebaseComponent }   from './knowledgebase/knowledgebase.component';
import { CodeExamplesComponent }   from './code-examples/code-examples.component';
import { AuthenticateComponent } from './authenticate/authenticate.component';
import { ChecklistComponent } from './checklist/checklist.component';
import { ChecklistEditComponent } from './checklist-edit/checklist-edit.component';
import { ChecklistManageComponent } from './checklist-manage/checklist-manage.component';
import { ChecklistSummaryComponent } from './checklist-summary/checklist-summary.component';
import { UserAddComponent } from './user-add/user-add.component';
import { GuardService } from './guard/guard.service';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { UserManageComponent } from './user-manage/user-manage.component';
import { StartsWithPipe } from './pipes/starts-with.pipe'
import { OrderBy } from './pipes/order-by.pipe'
import { HighlightJsModule, HighlightJsService } from 'angular2-highlight-js';
import { FirstLoginComponent } from './first-login/first-login.component';
import { UndefinedComponent } from './undefined/undefined.component';
import { QuestionnairePreComponent } from './questionnaire-pre/questionnaire-pre.component';


@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    HeaderComponent,
    FooterComponent,
    ProjectNewComponent,
    ProjectListComponent,
    ProjectDashboardComponent,
    ProjectSummaryComponent,
    ProjectSummaryAuditComponent,
    UserAddComponent,
    UserManageComponent,
    KnowledgebaseComponent,
    CodeExamplesComponent,
    AuthenticateComponent,
    ChecklistComponent,
    ChecklistManageComponent,
    ChecklistEditComponent,
    ChecklistSummaryComponent,
    StartsWithPipe,
    OrderBy,
    FirstLoginComponent,
    UndefinedComponent,
    QuestionnairePreComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ReactiveFormsModule,
    HighlightJsModule,
    AppRoutingModule,
    NgbModule.forRoot()
  ],
  providers: [GuardService,HighlightJsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
