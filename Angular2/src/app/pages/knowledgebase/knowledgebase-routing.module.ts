import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {LearnComponent} from './learn/learn.component';

const routes: Routes = [ {path: 'learn', component: LearnComponent}];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class KnowledgeBaseRoutingModule { }

