import { NgbCalendarHijri } from './ngb-calendar-hijri';
import { NgbDate } from '../ngb-date';
import { NgbPeriod } from '../ngb-calendar';
export declare class NgbCalendarIslamicCivil extends NgbCalendarHijri {
    /**
     * Returns the equivalent islamic(civil) date value for a give input Gregorian date.
     * `gdate` is a JS Date to be converted to Hijri.
     */
    fromGregorian(gdate: Date): NgbDate;
    /**
     * Returns the equivalent JS date value for a give input islamic(civil) date.
     * `hijriDate` is an islamic(civil) date to be converted to Gregorian.
     */
    toGregorian(hijriDate: NgbDate): Date;
    /**
     * Returns the number of days in a specific Hijri month.
     * `month` is 1 for Muharram, 2 for Safar, etc.
     * `year` is any Hijri year.
     */
    getDaysInIslamicMonth(month: number, year: number): number;
    getNext(date: NgbDate, period?: NgbPeriod, number?: number): NgbDate;
    getPrev(date: NgbDate, period?: NgbPeriod, number?: number): NgbDate;
    getWeekday(date: NgbDate): number;
    getWeekNumber(week: NgbDate[], firstDayOfWeek: number): number;
    getToday(): NgbDate;
}
