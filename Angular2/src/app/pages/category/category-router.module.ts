import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CategoryManageComponent } from './manage/manage.component';

const routes: Routes = [
    {path: 'manage', component: CategoryManageComponent}
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CategoryRoutingModule { }

