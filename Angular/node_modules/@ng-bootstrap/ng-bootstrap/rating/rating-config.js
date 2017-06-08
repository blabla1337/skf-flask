import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbRating component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the ratings used in the application.
 */
var NgbRatingConfig = (function () {
    function NgbRatingConfig() {
        this.max = 10;
        this.readonly = false;
    }
    return NgbRatingConfig;
}());
export { NgbRatingConfig };
NgbRatingConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbRatingConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=rating-config.js.map