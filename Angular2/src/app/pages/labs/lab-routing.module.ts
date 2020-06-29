import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LabViewComponent } from './view/view.component';
import { LabReadComponent } from './read/read.component';

const routes: Routes = [
    {path: 'view', component: LabViewComponent},
    {path: 'read', component: LabReadComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class LabsRoutingModule { }

