import { Injectable } from '@angular/core';
/**
 * Configuration service for the NgbDatepicker component.
 * You can inject this service, typically in your root component, and customize the values of its properties in
 * order to provide default values for all the datepickers used in the application.
 */
var NgbDatepickerConfig = (function () {
    function NgbDatepickerConfig() {
        this.displayMonths = 1;
        this.firstDayOfWeek = 1;
        this.navigation = 'select';
        this.outsideDays = 'visible';
        this.showWeekdays = true;
        this.showWeekNumbers = false;
    }
    return NgbDatepickerConfig;
}());
export { NgbDatepickerConfig };
NgbDatepickerConfig.decorators = [
    { type: Injectable },
];
/** @nocollapse */
NgbDatepickerConfig.ctorParameters = function () { return []; };
//# sourceMappingURL=datepicker-config.js.map