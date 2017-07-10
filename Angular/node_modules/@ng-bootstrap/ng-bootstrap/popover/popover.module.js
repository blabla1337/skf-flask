import { NgModule } from '@angular/core';
import { NgbPopover, NgbPopoverWindow } from './popover';
import { NgbPopoverConfig } from './popover-config';
export { NgbPopover } from './popover';
export { NgbPopoverConfig } from './popover-config';
var NgbPopoverModule = (function () {
    function NgbPopoverModule() {
    }
    NgbPopoverModule.forRoot = function () { return { ngModule: NgbPopoverModule, providers: [NgbPopoverConfig] }; };
    return NgbPopoverModule;
}());
export { NgbPopoverModule };
NgbPopoverModule.decorators = [
    { type: NgModule, args: [{ declarations: [NgbPopover, NgbPopoverWindow], exports: [NgbPopover], entryComponents: [NgbPopoverWindow] },] },
];
/** @nocollapse */
NgbPopoverModule.ctorParameters = function () { return []; };
//# sourceMappingURL=popover.module.js.map