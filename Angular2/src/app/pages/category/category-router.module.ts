import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { CategoryManageComponent } from './manage/manage.component';
import { UpdateCategoryComponent } from './update/update.component';
import { CreateCategoryComponent } from './create/create.component';

const routes: Routes = [
    {path: 'manage', component: CategoryManageComponent},
    {path: 'create', component: CreateCategoryComponent},
    {path: 'update', component: UpdateCategoryComponent},
];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class CategoryRoutingModule { }

