import { TemplateRef, QueryList, OnDestroy, AfterContentChecked, OnInit, EventEmitter } from '@angular/core';
import { NgbCarouselConfig } from './carousel-config';
/**
 * Represents an individual slide to be used within a carousel.
 */
export declare class NgbSlide {
    tplRef: TemplateRef<any>;
    /**
     * Unique slide identifier. Must be unique for the entire document for proper accessibility support.
     * Will be auto-generated if not provided.
     */
    id: string;
    constructor(tplRef: TemplateRef<any>);
}
/**
 * Directive to easily create carousels based on Bootstrap's markup.
 */
export declare class NgbCarousel implements AfterContentChecked, OnDestroy, OnInit {
    slides: QueryList<NgbSlide>;
    private _slideChangeInterval;
    /**
     * Amount of time in milliseconds before next slide is shown.
     */
    interval: number;
    /**
     * Whether can wrap from the last to the first slide.
     */
    wrap: boolean;
    /**
     * A flag for allowing navigation via keyboard
     */
    keyboard: boolean;
    /**
     * The active slide id.
     */
    activeId: string;
    /**
     * A carousel slide event fired when the slide transition is completed.
     * See NgbSlideEvent for payload details
     */
    slide: EventEmitter<NgbSlideEvent>;
    constructor(config: NgbCarouselConfig);
    ngAfterContentChecked(): void;
    ngOnInit(): void;
    ngOnDestroy(): void;
    /**
     * Navigate to a slide with the specified identifier.
     */
    select(slideId: string): void;
    /**
     * Navigate to the next slide.
     */
    prev(): void;
    /**
     * Navigate to the next slide.
     */
    next(): void;
    /**
     * Stops the carousel from cycling through items.
     */
    pause(): void;
    /**
     * Restarts cycling through the carousel slides from left to right.
     */
    cycle(): void;
    cycleToNext(): void;
    cycleToPrev(): void;
    cycleToSelected(slideIdx: string, direction: NgbSlideEventDirection): void;
    keyPrev(): void;
    keyNext(): void;
    private _restartTimer();
    private _startTimer();
    private _stopTimer();
    private _getSlideById(slideId);
    private _getSlideIdxById(slideId);
    private _getNextSlide(currentSlideId);
    private _getPrevSlide(currentSlideId);
    private _getSlideEventDirection(currentActiveSlideId, nextActiveSlideId);
}
/**
* The payload of the slide event fired when the slide transition is completed
*/
export interface NgbSlideEvent {
    /**
     * Previous slide id
     */
    prev: string;
    /**
     * New slide ids
     */
    current: string;
    /**
     * Slide event direction
     */
    direction: NgbSlideEventDirection;
}
/**
 * Enum to define the carousel slide event direction
 */
export declare enum NgbSlideEventDirection {
    LEFT,
    RIGHT,
}
export declare const NGB_CAROUSEL_DIRECTIVES: (typeof NgbSlide | typeof NgbCarousel)[];
