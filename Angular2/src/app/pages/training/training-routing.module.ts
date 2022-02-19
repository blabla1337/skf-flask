import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {TrainingMenuComponent} from './menu/menu.component';


const routes: Routes = [
  {path: 'menu', component: TrainingMenuComponent},
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class TrainingRoutingModule { }

