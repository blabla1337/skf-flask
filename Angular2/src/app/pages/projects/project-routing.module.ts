import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {ManageComponent} from './manage/manage.component';

const routes: Routes = [ {path: 'manage', component: ManageComponent}];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ProjectRoutingModule { }

