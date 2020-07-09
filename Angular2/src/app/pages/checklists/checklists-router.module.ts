import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewComponent } from './view/view.component';
import { ChecklistsReadComponent } from './read/read.component';
import { CheckManageComponent } from './manage/manage.component';

const routes: Routes = [
    {path: 'view', component: ViewComponent},
    {path: 'read', component: ChecklistsReadComponent},
    {path: 'manage', component: CheckManageComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ChecklistsRoutingModule {}
