import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbTabset component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the tabsets used in the application.
 */
var NgbTabsetConfig = (function () {
    function NgbTabsetConfig() {
        this.justify = 'start';
        this.type = 'tabs';
    }
    return NgbTabsetConfig;
}());
export { NgbTabsetConfig };
NgbTabsetConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbTabsetConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=tabset-config.js.map