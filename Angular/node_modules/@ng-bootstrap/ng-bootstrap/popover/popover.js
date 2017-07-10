import { Component, Directive, Input, Output, EventEmitter, ChangeDetectionStrategy, Injector, Renderer2, ElementRef, ViewContainerRef, ComponentFactoryResolver, NgZone } from '@angular/core';
import { listenToTriggers } from '../util/triggers';
import { positionElements } from '../util/positioning';
import { PopupService } from '../util/popup';
import { NgbPopoverConfig } from './popover-config';
var nextId = 0;
var NgbPopoverWindow = (function () {
    function NgbPopoverWindow() {
        this.placement = 'top';
    }
    return NgbPopoverWindow;
}());
export { NgbPopoverWindow };
NgbPopoverWindow.decorators = [
    { type: Component, args: [{
                selector: 'ngb-popover-window',
                changeDetection: ChangeDetectionStrategy.OnPush,
                host: { '[class]': '"popover show popover-" + placement', 'role': 'tooltip', '[id]': 'id' },
                template: "\n    <h3 class=\"popover-title\">{{title}}</h3><div class=\"popover-content\"><ng-content></ng-content></div>\n    "
            },] },
];
/** @nocollapse */
NgbPopoverWindow.ctorParameters = function () { return []; };
NgbPopoverWindow.propDecorators = {
    'placement': [{ type: Input },],
    'title': [{ type: Input },],
    'id': [{ type: Input },],
};
/**
 * A lightweight, extensible directive for fancy popover creation.
 */
var NgbPopover = (function () {
    function NgbPopover(_elementRef, _renderer, injector, componentFactoryResolver, viewContainerRef, config, ngZone) {
        var _this = this;
        this._elementRef = _elementRef;
        this._renderer = _renderer;
        /**
         * Emits an event when the popover is shown
         */
        this.shown = new EventEmitter();
        /**
         * Emits an event when the popover is hidden
         */
        this.hidden = new EventEmitter();
        this._ngbPopoverWindowId = "ngb-popover-" + nextId++;
        this.placement = config.placement;
        this.triggers = config.triggers;
        this.container = config.container;
        this._popupService = new PopupService(NgbPopoverWindow, injector, viewContainerRef, _renderer, componentFactoryResolver);
        this._zoneSubscription = ngZone.onStable.subscribe(function () {
            if (_this._windowRef) {
                positionElements(_this._elementRef.nativeElement, _this._windowRef.location.nativeElement, _this.placement, _this.container === 'body');
            }
        });
    }
    /**
     * Opens an element’s popover. This is considered a “manual” triggering of the popover.
     * The context is an optional value to be injected into the popover template when it is created.
     */
    NgbPopover.prototype.open = function (context) {
        if (!this._windowRef) {
            this._windowRef = this._popupService.open(this.ngbPopover, context);
            this._windowRef.instance.placement = this.placement;
            this._windowRef.instance.title = this.popoverTitle;
            this._windowRef.instance.id = this._ngbPopoverWindowId;
            this._renderer.setAttribute(this._elementRef.nativeElement, 'aria-describedby', this._ngbPopoverWindowId);
            if (this.container === 'body') {
                window.document.querySelector(this.container).appendChild(this._windowRef.location.nativeElement);
            }
            // position popover along the element
            positionElements(this._elementRef.nativeElement, this._windowRef.location.nativeElement, this.placement, this.container === 'body');
            // we need to manually invoke change detection since events registered via
            // Renderer::listen() are not picked up by change detection with the OnPush strategy
            this._windowRef.changeDetectorRef.markForCheck();
            this.shown.emit();
        }
    };
    /**
     * Closes an element’s popover. This is considered a “manual” triggering of the popover.
     */
    NgbPopover.prototype.close = function () {
        if (this._windowRef) {
            this._renderer.removeAttribute(this._elementRef.nativeElement, 'aria-describedby');
            this._popupService.close();
            this._windowRef = null;
            this.hidden.emit();
        }
    };
    /**
     * Toggles an element’s popover. This is considered a “manual” triggering of the popover.
     */
    NgbPopover.prototype.toggle = function () {
        if (this._windowRef) {
            this.close();
        }
        else {
            this.open();
        }
    };
    /**
     * Returns whether or not the popover is currently being shown
     */
    NgbPopover.prototype.isOpen = function () { return this._windowRef != null; };
    NgbPopover.prototype.ngOnInit = function () {
        this._unregisterListenersFn = listenToTriggers(this._renderer, this._elementRef.nativeElement, this.triggers, this.open.bind(this), this.close.bind(this), this.toggle.bind(this));
    };
    NgbPopover.prototype.ngOnDestroy = function () {
        this.close();
        this._unregisterListenersFn();
        this._zoneSubscription.unsubscribe();
    };
    return NgbPopover;
}());
export { NgbPopover };
NgbPopover.decorators = [
    { type: Directive, args: [{ selector: '[ngbPopover]', exportAs: 'ngbPopover' },] },
];
/** @nocollapse */
NgbPopover.ctorParameters = function () { return [
    { type: ElementRef, },
    { type: Renderer2, },
    { type: Injector, },
    { type: ComponentFactoryResolver, },
    { type: ViewContainerRef, },
    { type: NgbPopoverConfig, },
    { type: NgZone, },
]; };
NgbPopover.propDecorators = {
    'ngbPopover': [{ type: Input },],
    'popoverTitle': [{ type: Input },],
    'placement': [{ type: Input },],
    'triggers': [{ type: Input },],
    'container': [{ type: Input },],
    'shown': [{ type: Output },],
    'hidden': [{ type: Output },],
};
//# sourceMappingURL=popover.js.map