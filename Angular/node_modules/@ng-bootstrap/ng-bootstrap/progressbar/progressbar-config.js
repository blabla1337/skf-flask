import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbProgressbar component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the progress bars used in the application.
 */
var NgbProgressbarConfig = (function () {
    function NgbProgressbarConfig() {
        this.max = 100;
        this.animated = false;
        this.striped = false;
        this.showValue = false;
    }
    return NgbProgressbarConfig;
}());
export { NgbProgressbarConfig };
NgbProgressbarConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbProgressbarConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=progressbar-config.js.map