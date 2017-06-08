import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbAlert component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the alerts used in the application.
 */
var NgbAlertConfig = (function () {
    function NgbAlertConfig() {
        this.dismissible = true;
        this.type = 'warning';
    }
    return NgbAlertConfig;
}());
export { NgbAlertConfig };
NgbAlertConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbAlertConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=alert-config.js.map