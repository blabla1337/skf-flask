import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {TrainingProfilesComponent} from './profiles/training-profiles.component';
import {TrainingProfileComponent} from './profile/training-profile.component';
import {TrainingCourseComponent} from './course/training-course.component';


const routes: Routes = [
  {path: 'profiles', component: TrainingProfilesComponent},
  {path: 'profile/:id', component: TrainingProfileComponent},
  {path: 'course/:id', component: TrainingCourseComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TrainingRoutingModule { }