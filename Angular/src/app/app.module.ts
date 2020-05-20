/*
Dependencies:
https://ng-bootstrap.github.io/#/getting-started
npm install --save @ng-bootstrap/ng-bootstrap
npm install --save angular2-highlight-js



This we used in tje code to check claims in the JWT
and decide of we do/don't want to show certain elements in pages
this only makes sense with more roles which we currently don't support yet!

import { AppSettings } from '../globals';
import * as JWT from 'jwt-decode';

if (AppSettings.AUTH_TOKEN) {
  const decodedJWT = JWT(AppSettings.AUTH_TOKEN);
  this.canEdit = decodedJWT.privilege.includes('edit');
}



*/

import { BrowserModule } from '@angular/platform-browser';
import { NgModule, APP_INITIALIZER } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { LabsComponent } from './labs/labs.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { AppRoutingModule } from './app-routing.module';
import { ProjectListComponent } from './project-list/project-list.component';
import { ProjectDashboardComponent } from './project-dashboard/project-dashboard.component';
import { ProjectSummaryComponent } from './project-summary/project-summary.component';
import { PluginManagerComponent } from './plugin-manager/plugin-manager.component';
import { KnowledgebaseComponent } from './knowledgebase/knowledgebase.component';
import { KnowledgebaseEditComponent } from './knowledgebase-edit/knowledgebase-edit.component';
import { CodeExamplesComponent } from './code-examples/code-examples.component';
import { CodeExamplesEditComponent } from './code-examples-edit/code-examples-edit.component';
import { CategoryComponent } from './category-list/category-list.component';
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
import { LangFilterPipe } from './pipes/lang-filter.pipe';
import { LabelFilterPipe } from './pipes/label-filter.pipe';
import { filter } from 'rxjs/operators';
import { HighlightJsModule, HighlightJsService } from 'angular2-highlight-js';
import { FirstLoginComponent } from './first-login/first-login.component';
import { UndefinedComponent } from './undefined/undefined.component';
import { QuestionnaireComponent } from './questionnaire/questionnaire.component';
import { NgSelectModule } from '@ng-select/ng-select';
import { AuthModule, EventTypes, LogLevel, OidcConfigService, PublicEventsService } from 'angular-auth-oidc-client';

export function configureAuth(oidcConfigService: OidcConfigService)
{
  return () =>
    oidcConfigService.withConfig({
      stsServer: 'http://94ce817d.ngrok.io/auth/realms/new2',
      redirectUrl: window.location.origin + '/dashboard',
      postLogoutRedirectUri: window.location.origin + '/login',
      clientId: 'test',
      scope: 'openid email',
      responseType: 'code',
      silentRenew: true,
      silentRenewUrl: `${window.location.origin}/silent-renew.html`,
      renewTimeBeforeTokenExpiresInSeconds: 50,
      logLevel: LogLevel.Debug,
    });
}

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    HeaderComponent,
    FooterComponent,
    ProjectListComponent,
    ProjectDashboardComponent,
    ProjectSummaryComponent,
    PluginManagerComponent,
    UserAddComponent,
    UserManageComponent,
    KnowledgebaseComponent,
    KnowledgebaseEditComponent,
    CodeExamplesComponent,
    CodeExamplesEditComponent,
    CategoryComponent,
    AuthenticateComponent,
    ChecklistComponent,
    ChecklistManageComponent,
    ChecklistEditComponent,
    ChecklistAddNewComponent,
    ChecklistSummaryComponent,
    StartsWithPipe,
    OrderBy,
    StringFilterPipe,
    LangFilterPipe,
    LabelFilterPipe,
    FirstLoginComponent,
    UndefinedComponent,
    LabsComponent,
    QuestionnaireComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    ReactiveFormsModule,
    HighlightJsModule,
    AppRoutingModule,
    NgbModule.forRoot(),
    AuthModule.forRoot(),
    NgSelectModule
  ],
  providers: [GuardService, HighlightJsService, OidcConfigService,
    {
      provide: APP_INITIALIZER,
      useFactory: configureAuth,
      deps: [OidcConfigService],
      multi: true,
    },],
  bootstrap: [AppComponent]
})

export class AppModule
{
  constructor(private readonly eventService: PublicEventsService)
  {
    this.eventService
      .registerForEvents()
      .pipe(filter((notification) => notification.type === EventTypes.ConfigLoaded))
      .subscribe((config) => console.log('ConfigLoaded', config));
  }
}
