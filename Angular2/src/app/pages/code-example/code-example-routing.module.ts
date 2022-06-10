import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewCodeComponent } from './view/view.component';
import { CreateCodeComponent } from './create/create.component';
import { UpdateCodeComponent } from './update/update.component';
import { HardLinkCodeComponent } from './hard-link/hard-link.component';

const routes: Routes = [
    { path: 'view', component: ViewCodeComponent },
    { path: 'create', component: CreateCodeComponent },
    { path: 'update/:id', component: UpdateCodeComponent },
    { path: 'hard-link/:id', component: HardLinkCodeComponent }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CodeExampleRoutingModule { }
