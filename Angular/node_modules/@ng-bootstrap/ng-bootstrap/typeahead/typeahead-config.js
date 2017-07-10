import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbTypeahead component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the typeaheads used in the application.
 */
var NgbTypeaheadConfig = (function () {
    function NgbTypeaheadConfig() {
        this.editable = true;
        this.focusFirst = true;
        this.showHint = false;
    }
    return NgbTypeaheadConfig;
}());
export { NgbTypeaheadConfig };
NgbTypeaheadConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbTypeaheadConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=typeahead-config.js.map