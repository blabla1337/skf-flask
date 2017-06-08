import { NgModule } from '@angular/core';
import { NgbDropdown, NgbDropdownToggle } from './dropdown';
import { NgbDropdownConfig } from './dropdown-config';
export { NgbDropdown, NgbDropdownToggle } from './dropdown';
export { NgbDropdownConfig } from './dropdown-config';
var NGB_DROPDOWN_DIRECTIVES = [NgbDropdownToggle, NgbDropdown];
var NgbDropdownModule = (function () {
    function NgbDropdownModule() {
    }
    NgbDropdownModule.forRoot = function () { return { ngModule: NgbDropdownModule, providers: [NgbDropdownConfig] }; };
    return NgbDropdownModule;
}());
export { NgbDropdownModule };
NgbDropdownModule.decorators = [
    { type: NgModule, args: [{ declarations: NGB_DROPDOWN_DIRECTIVES, exports: NGB_DROPDOWN_DIRECTIVES },] },
];
/** @nocollapse */
NgbDropdownModule.ctorParameters = function () { return []; };
//# sourceMappingURL=dropdown.module.js.map