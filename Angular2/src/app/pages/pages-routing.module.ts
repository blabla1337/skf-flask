import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './dashboard/home/home.component';
import { LoggedInAuthGuard } from '../core/guards/loggedinguard.service';

export const routes: Routes = [
  { path: '', redirectTo: 'dashboard', pathMatch: 'full'},
  { path: 'dashboard', component: HomeComponent, canActivate: [LoggedInAuthGuard] },
  { path: 'users', loadChildren: () => import('./users/users.module').then(m => m.UsersModule), canActivate: [LoggedInAuthGuard] },
  { path: 'code-example', loadChildren: () => import('./code-example/code-example.module').then(m => m.CodeExampleModule), canActivate: [LoggedInAuthGuard] },
  { path: 'knowledgebase', loadChildren: () => import('./knowledgebase/knowledgebase.module').then(m => m.KnowledgebaseModule), canActivate: [LoggedInAuthGuard] },
  { path: 'checklists', loadChildren: () => import('./checklists/checklists.module').then(m => m.ChecklistsModule), canActivate: [LoggedInAuthGuard] },
  { path: 'projects', loadChildren: () => import('./projects/projects.module').then(m => m.ProjectsModule), canActivate: [LoggedInAuthGuard] },
  { path: 'labs', loadChildren: () => import('./labs/labs.module').then(m => m.LabsModule), canActivate: [LoggedInAuthGuard] },
  { path: 'search', loadChildren: () => import('./search/search.module').then(m => m.SearchModule), canActivate: [LoggedInAuthGuard] },
  { path: 'category', loadChildren: () => import('./category/category.module').then(m => m.CategoryModule), canActivate: [LoggedInAuthGuard] },
  { path: 'training', loadChildren: () => import('./training/training.module').then(m => m.TrainingModule), canActivate: [LoggedInAuthGuard] },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule { }
