import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbTabset, NgbTab, NgbTabContent, NgbTabTitle } from './tabset';
import { NgbTabsetConfig } from './tabset-config';
export { NgbTabset, NgbTab, NgbTabContent, NgbTabTitle } from './tabset';
export { NgbTabsetConfig } from './tabset-config';
var NGB_TABSET_DIRECTIVES = [NgbTabset, NgbTab, NgbTabContent, NgbTabTitle];
var NgbTabsetModule = (function () {
    function NgbTabsetModule() {
    }
    NgbTabsetModule.forRoot = function () { return { ngModule: NgbTabsetModule, providers: [NgbTabsetConfig] }; };
    return NgbTabsetModule;
}());
export { NgbTabsetModule };
NgbTabsetModule.decorators = [
    { type: NgModule, args: [{ declarations: NGB_TABSET_DIRECTIVES, exports: NGB_TABSET_DIRECTIVES, imports: [CommonModule] },] },
];
/** @nocollapse */
NgbTabsetModule.ctorParameters = function () { return []; };
//# sourceMappingURL=tabset.module.js.map