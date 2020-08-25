import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { HighlightModule, HIGHLIGHT_OPTIONS } from 'ngx-highlightjs';
import { JoyrideModule } from 'ngx-joyride';

import { NgbNavModule, NgbAccordionModule, NgbTooltipModule } from '@ng-bootstrap/ng-bootstrap';

import { AuthGuard } from './core/guards/guard.service';
import { LoggedInAuthGuard } from './core/guards/loggedinguard.service';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LayoutsModule } from './layouts/layouts.module';
import { HomeComponent } from './pages/dashboard/home/home.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    NgbModule,
    LayoutsModule,
    NgbAccordionModule,
    NgbNavModule,
    NgbTooltipModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    HighlightModule,
    JoyrideModule.forRoot(),
  ],
  providers: [ AuthGuard, LoggedInAuthGuard,
    {
      provide: HIGHLIGHT_OPTIONS,
      useValue: {
        coreLibraryLoader: () => import('highlight.js/lib/core'),
        lineNumbersLoader: () => import('highlightjs-line-numbers.js'), // Optional, only if you want the line numbers
        lineNumbers: true,
        languages: {
          python: () => import('highlight.js/lib/languages/python'),
          css: () => import('highlight.js/lib/languages/css'),
          xml: () => import('highlight.js/lib/languages/xml'),
          ruby: () => import('highlight.js/lib/languages/ruby'),
          django: () => import('highlight.js/lib/languages/django'),
          java: () => import('highlight.js/lib/languages/java'),
          php: () => import('highlight.js/lib/languages/php'),
        }
      }
    }
  ],  bootstrap: [AppComponent]
})
export class AppModule { }
