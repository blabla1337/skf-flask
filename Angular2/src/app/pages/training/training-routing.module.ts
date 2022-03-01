import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {TrainingProfilesComponent} from './profiles/training-profiles.component';
import {TrainingProfileComponent} from './profile/training-profile.component';


const routes: Routes = [
  {path: 'profiles', component: TrainingProfilesComponent},
  {path: 'profile/:id', component: TrainingProfileComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TrainingRoutingModule { }
