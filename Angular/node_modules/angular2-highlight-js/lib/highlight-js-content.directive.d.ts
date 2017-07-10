import { ElementRef, OnInit, AfterViewChecked, NgZone } from '@angular/core';
export declare class HighlightJsContentDirective implements OnInit, AfterViewChecked {
    private elementRef;
    private zone;
    useBr: boolean;
    highlightSelector: string;
    constructor(elementRef: ElementRef, zone: NgZone);
    ngOnInit(): void;
    ngAfterViewChecked(): void;
}
