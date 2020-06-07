import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './dashboard/home/home.component';
const routes: Routes = [
  { path: '', redirectTo: 'dashboard' },
  { path: 'dashboard', component: HomeComponent },
  { path: 'dashboards', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
