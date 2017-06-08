import { NgModule } from '@angular/core';
import { NgbTooltip, NgbTooltipWindow } from './tooltip';
import { NgbTooltipConfig } from './tooltip-config';
export { NgbTooltipConfig } from './tooltip-config';
export { NgbTooltip } from './tooltip';
var NgbTooltipModule = (function () {
    function NgbTooltipModule() {
    }
    NgbTooltipModule.forRoot = function () { return { ngModule: NgbTooltipModule, providers: [NgbTooltipConfig] }; };
    return NgbTooltipModule;
}());
export { NgbTooltipModule };
NgbTooltipModule.decorators = [
    { type: NgModule, args: [{ declarations: [NgbTooltip, NgbTooltipWindow], exports: [NgbTooltip], entryComponents: [NgbTooltipWindow] },] },
];
/** @nocollapse */
NgbTooltipModule.ctorParameters = function () { return []; };
//# sourceMappingURL=tooltip.module.js.map