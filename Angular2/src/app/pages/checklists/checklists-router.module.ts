import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewComponent } from './view/view.component';
import { ChecklistsReadComponent } from './read/read.component';
import { CheckManageComponent } from './manage/manage.component';
import { ChecklistCreateComponent } from './create/create.component';
import { AddChecklistComponent } from './add-checklist/add-checklist.component';
import { UpdateChecklistComponent } from './update-checklist/update-checklist.component';
import { UpdateQuestionnaireComponent } from './questionnaire/update/update.component';
import { CreateQuestionnaireComponent } from './questionnaire/create/create.component';
import { UpdateChecklistTypeComponent } from './checklist-type/update/update.component';
import { CreateChecklistTypeComponent } from './checklist-type/create/create.component';

const routes: Routes = [
    { path: 'view', component: ViewComponent },
    { path: 'read/:id', component: ChecklistsReadComponent },
    { path: 'manage', component: CheckManageComponent },
    { path: 'create', component: ChecklistCreateComponent },
    { path: 'add', component: AddChecklistComponent },
    { path: 'update/:id', component: UpdateChecklistComponent },
    { path: 'question-update/:id', component: UpdateQuestionnaireComponent },
    { path: 'question-create', component: CreateQuestionnaireComponent },
    { path: 'checklist-type-create', component: CreateChecklistTypeComponent },
    { path: 'checklist-type-update/:id', component: UpdateChecklistTypeComponent },
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ChecklistsRoutingModule { }
