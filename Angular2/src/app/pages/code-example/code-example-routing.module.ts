import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {CodeViewComponent} from './view/view.component';
import {EditComponent} from './edit/edit.component';
import { CodeCreateComponent } from './create/create.component';

const routes: Routes = [
    {path: 'view', component: CodeViewComponent},
    {path: 'edit', component: EditComponent},
    {path: 'create', component: CodeCreateComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CodeExampleRoutingModule {}
