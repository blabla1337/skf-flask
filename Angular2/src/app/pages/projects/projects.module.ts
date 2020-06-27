import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProjectRoutingModule } from './project-routing.module';
import { ViewComponent } from './view/view.component';

@NgModule({
  declarations: [ViewComponent],
  imports: [
    CommonModule,
    ProjectRoutingModule
  ]
})
export class ProjectsModule { }
