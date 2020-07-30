import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import {ManageComponent} from './manage/manage.component';
import {UserCreateComponent} from './create/create.component';
import {UserUpdateComponent} from './update/update.component';

const routes: Routes = [ {path: 'manage', component: ManageComponent},
                         {path: 'create', component: UserCreateComponent},
                         {path: 'update', component: UserUpdateComponent}
                        ];

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
})
export class UsersRoutingModule { }
