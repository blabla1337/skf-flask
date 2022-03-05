import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TrainingRoutingModule } from './training-routing.module';
import { TrainingProfilesComponent } from './profiles/training-profiles.component';
import { TrainingCourseComponent } from './course/training-course.component';
import { TrainingProfileComponent } from './profile/training-profile.component';
import { TrainingCourseTreeComponent } from './course-tree/training-course-tree.component';
import { TrainingCourseContentComponent } from './course-content/training-course-content.component';
import {TreeModule} from '@circlon/angular-tree-component';


@NgModule({
  declarations: [
    TrainingProfilesComponent,
    TrainingCourseComponent,
    TrainingProfileComponent,
    TrainingCourseTreeComponent,
    TrainingCourseContentComponent,
  ],
  imports: [
    CommonModule,
    TrainingRoutingModule,
    TreeModule
  ]
})
export class TrainingModule { }
