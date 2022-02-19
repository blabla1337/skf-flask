import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TrainingRoutingModule } from './training-routing.module';
import { TrainingProfilesComponent } from './profiles/training-profiles.component';
import { TrainingMainComponent } from './main/training-main.component';


@NgModule({
  declarations: [
    TrainingProfilesComponent,
    TrainingMainComponent
  ],
  imports: [
    CommonModule,
    TrainingRoutingModule,
  ]
})
export class TrainingModule { }
