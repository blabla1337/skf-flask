import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {CodeViewComponent} from './view/view.component';

const routes: Routes = [ {path: 'view', component: CodeViewComponent}];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CodeExampleRoutingModule {}
