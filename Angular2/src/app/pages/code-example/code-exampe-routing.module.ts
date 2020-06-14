import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {CodeExampleComponent} from './code-example.component';

const routes: Routes = [ {path: 'manage', component: CodeExampleComponent}];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CodeExampleRouting {}