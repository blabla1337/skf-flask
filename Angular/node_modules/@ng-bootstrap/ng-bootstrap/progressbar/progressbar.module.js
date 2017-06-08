import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbProgressbar } from './progressbar';
import { NgbProgressbarConfig } from './progressbar-config';
export { NgbProgressbar } from './progressbar';
export { NgbProgressbarConfig } from './progressbar-config';
var NgbProgressbarModule = (function () {
    function NgbProgressbarModule() {
    }
    NgbProgressbarModule.forRoot = function () { return { ngModule: NgbProgressbarModule, providers: [NgbProgressbarConfig] }; };
    return NgbProgressbarModule;
}());
export { NgbProgressbarModule };
NgbProgressbarModule.decorators = [
    { type: NgModule, args: [{ declarations: [NgbProgressbar], exports: [NgbProgressbar], imports: [CommonModule] },] },
];
/** @nocollapse */
NgbProgressbarModule.ctorParameters = function () { return []; };
//# sourceMappingURL=progressbar.module.js.map