import { NgModule } from '@angular/core';
import { NgbRadio, NgbActiveLabel, NgbRadioGroup } from './radio';
export { NgbRadio, NgbActiveLabel, NgbRadioGroup } from './radio';
var NGB_RADIO_DIRECTIVES = [NgbRadio, NgbActiveLabel, NgbRadioGroup];
var NgbButtonsModule = (function () {
    function NgbButtonsModule() {
    }
    NgbButtonsModule.forRoot = function () { return { ngModule: NgbButtonsModule, providers: [] }; };
    return NgbButtonsModule;
}());
export { NgbButtonsModule };
NgbButtonsModule.decorators = [
    { type: NgModule, args: [{ declarations: NGB_RADIO_DIRECTIVES, exports: NGB_RADIO_DIRECTIVES },] },
];
/** @nocollapse */
NgbButtonsModule.ctorParameters = function () { return []; };
//# sourceMappingURL=radio.module.js.map