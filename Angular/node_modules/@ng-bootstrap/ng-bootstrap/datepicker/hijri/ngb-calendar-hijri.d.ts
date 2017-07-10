import { NgbDate } from '../ngb-date';
import { NgbPeriod, NgbCalendar } from '../ngb-calendar';
export declare abstract class NgbCalendarHijri extends NgbCalendar {
    getDaysPerWeek(): number;
    getMonths(): number[];
    getWeeksPerMonth(): number;
    isValid(date: NgbDate): boolean;
    setDay(date: NgbDate, day: number): NgbDate;
    setMonth(date: NgbDate, month: number): NgbDate;
    setYear(date: NgbDate, yearValue: number): NgbDate;
    abstract getWeekday(date: NgbDate): number;
    abstract getNext(date: NgbDate, period?: NgbPeriod, number?: number): NgbDate;
    abstract getPrev(date: NgbDate, period?: NgbPeriod, number?: number): NgbDate;
    abstract getWeekNumber(week: NgbDate[], firstDayOfWeek: number): number;
    abstract getToday(): NgbDate;
    /**
     * Returns the equivalent Hijri date value for a give input Gregorian date.
     * `gDate` is s JS Date to be converted to Hijri.
     */
    abstract fromGregorian(gDate: Date): NgbDate;
    /**
     * Converts the current Hijri date to Gregorian.
     */
    abstract toGregorian(hijriDate: NgbDate): Date;
    /**
     * Returns the number of days in a specific Hijri month.
     * `month` is 1 for Muharram, 2 for Safar, etc.
     * `year` is any Hijri year.
     */
    abstract getDaysInIslamicMonth(month: number, year: number): number;
    protected _isIslamicLeapYear(year: number): boolean;
    /**
     * Returns the start of Hijri Month.
     * `month` is 0 for Muharram, 1 for Safar, etc.
     * `year` is any Hijri year.
     */
    protected _getMonthStart(year: number, month: number): number;
    /**
     * Returns the start of Hijri year.
     * `year` is any Hijri year.
     */
    protected _getYearStart(year: number): number;
}
