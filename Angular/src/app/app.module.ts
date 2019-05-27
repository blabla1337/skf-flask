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

import { MarkdownModule, MarkedOptions } from 'ngx-markdown';
import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LabsComponent } from './labs/labs.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { AppRoutingModule } from './app-routing.module';
import { ProjectNewComponent } from './project-new/project-new.component';
import { ProjectListComponent } from './project-list/project-list.component';
import { ProjectDashboardComponent }   from './project-dashboard/project-dashboard.component';
import { ProjectSummaryComponent }   from './project-summary/project-summary.component';
import { ProjectSummaryAuditComponent }   from './project-summary-audit/project-summary-audit.component';
import { KnowledgebaseComponent }   from './knowledgebase/knowledgebase.component';
import { KnowledgebaseEditComponent }   from './knowledgebase-edit/knowledgebase-edit.component';
import { CodeExamplesComponent }   from './code-examples/code-examples.component';
import { AuthenticateComponent } from './authenticate/authenticate.component';
import { ChecklistComponent } from './checklist/checklist.component';
import { ChecklistEditComponent } from './checklist-edit/checklist-edit.component';
import { ChecklistAddNewComponent } from './checklist-add-new/checklist-add-new.component';
import { ChecklistManageComponent } from './checklist-manage/checklist-manage.component';
import { ChecklistSummaryComponent } from './checklist-summary/checklist-summary.component';
import { UserAddComponent } from './user-add/user-add.component';
import { GuardService } from './guard/guard.service';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { UserManageComponent } from './user-manage/user-manage.component';
import { StartsWithPipe } from './pipes/starts-with.pipe';
import { OrderBy } from './pipes/order-by.pipe';
import { StringFilterPipe } from './pipes/string-filter.pipe';

import { HighlightJsModule, HighlightJsService } from 'angular2-highlight-js';
import { FirstLoginComponent } from './first-login/first-login.component';
import { UndefinedComponent } from './undefined/undefined.component';
import { QuestionnairePreComponent } from './questionnaire-pre/questionnaire-pre.component';
import { QuestionnaireSprintComponent } from './questionnaire-sprint/questionnaire-sprint.component';
import { NgSelectModule } from '@ng-select/ng-select';

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
    KnowledgebaseEditComponent,
    CodeExamplesComponent,
    AuthenticateComponent,
    ChecklistComponent,
    ChecklistManageComponent,
    ChecklistEditComponent,
    ChecklistAddNewComponent,
    ChecklistSummaryComponent,
    StartsWithPipe,
    OrderBy,
    StringFilterPipe,
    FirstLoginComponent,
    UndefinedComponent,
    QuestionnairePreComponent,
    LabsComponent,
    QuestionnaireSprintComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ReactiveFormsModule,
    HighlightJsModule,
    AppRoutingModule,
    NgbModule.forRoot(),
    MarkdownModule.forRoot({
      markedOptions: {
        provide: MarkedOptions,
        useValue: {
          gfm: true,
          tables: true,
          breaks: false,
          pedantic: false,
          sanitize: false,
          smartLists: true,
          smartypants: false,
        },
      },
    }),
    NgSelectModule
  ],
  providers: [GuardService,HighlightJsService],
  bootstrap: [AppComponent]
})
export class AppModule { }
