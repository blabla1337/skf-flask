import { NgModule } from '@angular/core';
import { NgbCollapse } from './collapse';
export { NgbCollapse } from './collapse';
var NgbCollapseModule = (function () {
    function NgbCollapseModule() {
    }
    NgbCollapseModule.forRoot = function () { return { ngModule: NgbCollapseModule, providers: [] }; };
    return NgbCollapseModule;
}());
export { NgbCollapseModule };
NgbCollapseModule.decorators = [
    { type: NgModule, args: [{ declarations: [NgbCollapse], exports: [NgbCollapse] },] },
];
/** @nocollapse */
NgbCollapseModule.ctorParameters = function () { return []; };
//# sourceMappingURL=collapse.module.js.map