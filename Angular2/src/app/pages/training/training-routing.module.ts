import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TrainingMainComponent } from './main/training-main.component';
import {TrainingProfilesComponent} from './profiles/training-profiles.component';


const routes: Routes = [
  {path: 'profiles', component: TrainingProfilesComponent},
  {path: 'learning', component: TrainingMainComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TrainingRoutingModule { }
