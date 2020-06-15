import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {ViewComponent} from './view/view.component';

const routes: Routes = [ {path: 'view', component: ViewComponent}];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CodeExampleRoutingModule {}
