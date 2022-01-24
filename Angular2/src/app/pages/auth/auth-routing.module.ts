import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { OpenidComponent } from './openid/openid.component';

const routes: Routes = [
    {path: 'login', component: LoginComponent},
    {path: 'openid', component: OpenidComponent},

];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})

export class AuthRoutingModule { }
