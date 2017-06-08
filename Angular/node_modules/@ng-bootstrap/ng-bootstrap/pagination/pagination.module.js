import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbPagination } from './pagination';
import { NgbPaginationConfig } from './pagination-config';
export { NgbPagination } from './pagination';
export { NgbPaginationConfig } from './pagination-config';
var NgbPaginationModule = (function () {
    function NgbPaginationModule() {
    }
    NgbPaginationModule.forRoot = function () { return { ngModule: NgbPaginationModule, providers: [NgbPaginationConfig] }; };
    return NgbPaginationModule;
}());
export { NgbPaginationModule };
NgbPaginationModule.decorators = [
    { type: NgModule, args: [{ declarations: [NgbPagination], exports: [NgbPagination], imports: [CommonModule] },] },
];
/** @nocollapse */
NgbPaginationModule.ctorParameters = function () { return []; };
//# sourceMappingURL=pagination.module.js.map