import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewComponent } from './view/view.component';
import { ChecklistsReadComponent } from './read/read.component';
import { CheckManageComponent } from './manage/manage.component';
import { ChecklistCreateComponent } from './create/create.component';
import { AddChecklistComponent } from './addchecklist/addchecklist.component';
import { UpdateChecklistComponent } from './updatechecklist/updatechecklist.component';
import { UpdateQuestionarieComponent } from './questionarie/update/update.component';
import { CreateQuestionarieComponent } from './questionarie/create/create.component';
import { UpdateCheckComponent } from './items/update/update.component';
import { CreateCheckComponent } from './items/create/create.component';

const routes: Routes = [
    { path: 'view', component: ViewComponent },
    { path: 'read/:id', component: ChecklistsReadComponent },
    { path: 'manage', component: CheckManageComponent },
    { path: 'create', component: ChecklistCreateComponent },
    { path: 'add', component: AddChecklistComponent },
    { path: 'update', component: UpdateChecklistComponent },
    { path: 'quest-update', component: UpdateQuestionarieComponent },
    { path: 'quest-create', component: CreateQuestionarieComponent },
    { path: 'check-create', component: CreateCheckComponent },
    { path: 'check-update', component: UpdateCheckComponent },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ChecklistsRoutingModule { }
