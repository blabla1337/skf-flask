import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TrainingRoutingModule } from './training-routing.module';
import { TrainingProfilesComponent } from './profiles/training-profiles.component';
import { TrainingMainComponent } from './main/training-main.component';
import { TrainingProfileComponent } from './profile/training-profile.component';


@NgModule({
  declarations: [
    TrainingProfilesComponent,
    TrainingMainComponent,
    TrainingProfileComponent,
  ],
  imports: [
    CommonModule,
    TrainingRoutingModule,
  ]
})
export class TrainingModule { }
