import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NgbTimepicker } from './timepicker';
import { NgbTimepickerConfig } from './timepicker-config';
export { NgbTimepicker } from './timepicker';
export { NgbTimepickerConfig } from './timepicker-config';
var NgbTimepickerModule = (function () {
    function NgbTimepickerModule() {
    }
    NgbTimepickerModule.forRoot = function () { return { ngModule: NgbTimepickerModule, providers: [NgbTimepickerConfig] }; };
    return NgbTimepickerModule;
}());
export { NgbTimepickerModule };
NgbTimepickerModule.decorators = [
    { type: NgModule, args: [{ declarations: [NgbTimepicker], exports: [NgbTimepicker], imports: [CommonModule] },] },
];
/** @nocollapse */
NgbTimepickerModule.ctorParameters = function () { return []; };
//# sourceMappingURL=timepicker.module.js.map