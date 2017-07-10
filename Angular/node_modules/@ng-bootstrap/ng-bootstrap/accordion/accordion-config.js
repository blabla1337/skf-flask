import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbAccordion component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the accordions used in the application.
 */
var NgbAccordionConfig = (function () {
    function NgbAccordionConfig() {
        this.closeOthers = false;
    }
    return NgbAccordionConfig;
}());
export { NgbAccordionConfig };
NgbAccordionConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbAccordionConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=accordion-config.js.map