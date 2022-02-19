import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { TrainingProfilesComponent } from './profiles/training-profiles.component';
import { TrainingMainComponent } from './main/training-main.component';


const routes: Routes = [
  {path: 'profiles', component: TrainingProfilesComponent},
  {path: 'learning', component: TrainingMainComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TrainingRoutingModule { }
