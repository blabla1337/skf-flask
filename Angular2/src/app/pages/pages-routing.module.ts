import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './dashboard/home/home.component';
const routes: Routes = [
  { path: '', redirectTo: 'dashboard' },
  { path: 'dashboard', component: HomeComponent },
  { path: 'dashboards', loadChildren: () => import('./dashboard/dashboard.module').then(m => m.DashboardModule) },
  { path: 'users', loadChildren: () => import('./users/users.module').then(m => m.UsersModule) },
  { path: 'code-example', loadChildren: () => import('./code-example/code-example.module').then(m => m.CodeExampleModule) },
  { path: 'knowledgebase', loadChildren: () => import('./knowledgebase/knowledgebase.module').then(m => m.KnowledgebaseModule) },
  { path: 'checklists', loadChildren: () => import('./checklists/checklists.module').then(m => m.ChecklistsModule) },
  { path: 'projects', loadChildren: () => import('./projects/projects.module').then(m => m.ProjectsModule) }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
