import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { ViewKnowledebaseComponent } from './view/view.component';
import { CreateComponent } from './create/create.component';
import { UpdateComponent } from './update/update.component';
import { HardLinkKBComponent } from './hard-link/hard-link.component';

const routes: Routes = [
    { path: 'view', component: ViewKnowledebaseComponent },
    { path: 'create', component: CreateComponent },
    { path: 'update/:id', component: UpdateComponent },
    { path: 'hard-link/:id', component: HardLinkKBComponent }
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class KnowledgeBaseRoutingModule { }

