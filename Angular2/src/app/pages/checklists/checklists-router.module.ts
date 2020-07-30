import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewComponent } from './view/view.component';
import { ChecklistsReadComponent } from './read/read.component';
import { CheckManageComponent } from './manage/manage.component';
import { ChecklistCreateComponent } from './create/create.component';
import { AddChecklistComponent } from './addchecklist/addchecklist.component';
import { UpdateChecklistComponent } from './updatechecklist/updatechecklist.component';

const routes: Routes = [
    {path: 'view', component: ViewComponent},
    {path: 'read', component: ChecklistsReadComponent},
    {path: 'manage', component: CheckManageComponent},
    {path: 'create', component: ChecklistCreateComponent},
    {path: 'add', component: AddChecklistComponent},
    {path: 'update', component: UpdateChecklistComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ChecklistsRoutingModule {}
