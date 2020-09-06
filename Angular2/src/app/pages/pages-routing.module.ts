import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './dashboard/home/home.component';

import { AuthGuard } from '../core/guards/guard.service';
import { LoggedInAuthGuard } from '../core/guards/loggedinguard.service';

export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
  { path: 'dashboard', component: HomeComponent },
  { path: 'users', loadChildren: () => import('./users/users.module').then(m => m.UsersModule) },
  { path: 'code-example', loadChildren: () => import('./code-example/code-example.module').then(m => m.CodeExampleModule) },
  { path: 'knowledgebase', loadChildren: () => import('./knowledgebase/knowledgebase.module').then(m => m.KnowledgebaseModule) },
  { path: 'checklists', loadChildren: () => import('./checklists/checklists.module').then(m => m.ChecklistsModule) },
  { path: 'projects', loadChildren: () => import('./projects/projects.module').then(m => m.ProjectsModule), canActivate: [AuthGuard] },
  { path: 'labs', loadChildren: () => import('./labs/labs.module').then(m => m.LabsModule) },
  { path: 'search', loadChildren: () => import('./search/search.module').then(m => m.SearchModule) },
  { path: 'category', loadChildren: () => import('./category/category.module').then(m => m.CategoryModule) },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
