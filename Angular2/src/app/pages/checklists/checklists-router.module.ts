import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {ViewComponent} from './view/view.component';
import { ChecklistsReadComponent } from './read/read.component';

const routes: Routes = [
    {path: 'view', component: ViewComponent},
    {path: 'read', component: ChecklistsReadComponent}
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class ChecklistsRoutingModule {}
