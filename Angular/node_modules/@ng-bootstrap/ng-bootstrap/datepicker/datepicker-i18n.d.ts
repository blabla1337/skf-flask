/**
 * Type of the service supplying month and weekday names to to NgbDatepicker component.
 * See the i18n demo for how to extend this class and define a custom provider for i18n.
 */
export declare abstract class NgbDatepickerI18n {
    /**
     * Returns the short weekday name to display in the heading of the month view.
     * With default calendar we use ISO 8601: 'weekday' is 1=Mon ... 7=Sun
     */
    abstract getWeekdayShortName(weekday: number): string;
    /**
     * Returns the short month name to display in the date picker navigation.
     * With default calendar we use ISO 8601: 'month' is 1=Jan ... 12=Dec
     */
    abstract getMonthShortName(month: number): string;
    /**
     * Returns the full month name to display in the date picker navigation.
     * With default calendar we use ISO 8601: 'month' is 1=January ... 12=December
     */
    abstract getMonthFullName(month: number): string;
}
export declare class NgbDatepickerI18nDefault extends NgbDatepickerI18n {
    getWeekdayShortName(weekday: number): string;
    getMonthShortName(month: number): string;
    getMonthFullName(month: number): string;
}
