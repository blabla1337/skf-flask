import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {ProjectManageComponent} from './manage/manage.component';
import {ProjectViewComponent} from './view/view.component';

const routes: Routes = [ 
    {path: 'manage', component: ProjectManageComponent},
    {path: 'view', component: ProjectViewComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ProjectRoutingModule { }

