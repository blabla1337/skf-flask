import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LabViewComponent } from './view/view.component';

const routes: Routes = [
    {path: 'view', component: LabViewComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class LabsRoutingModule { }

