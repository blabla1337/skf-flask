import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LayoutComponent } from './layouts/layout.component';
import { Page404Component } from './pages/extra/page404/page404.component';
import { Page500Component } from './pages/extra/page500/page500.component';

import { LoggedInAuthGuard } from './core/guards/loggedinguard.service';

const routes: Routes = [
  { path: '', component: LayoutComponent, loadChildren: () => import('./pages/pages.module').then(m => m.PagesModule)},
  { path: 'auth', loadChildren: () => import('./pages/auth/auth.module').then(m => m.AuthModule), canActivate: [LoggedInAuthGuard] },
  { path: 'page-404', component: Page404Component},
  { path: 'page-500', component: Page500Component},
  { path: '**', redirectTo: '/page-404', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }
