import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TrainingRoutingModule } from './training-routing.module';
import { TrainingProfilesComponent } from './profiles/training-profiles.component';
import { TrainingCourseComponent } from './course/training-course.component';
import { TrainingProfileComponent } from './profile/training-profile.component';


@NgModule({
  declarations: [
    TrainingProfilesComponent,
    TrainingCourseComponent,
    TrainingProfileComponent,
  ],
  imports: [
    CommonModule,
    TrainingRoutingModule,
  ]
})
export class TrainingModule { }
