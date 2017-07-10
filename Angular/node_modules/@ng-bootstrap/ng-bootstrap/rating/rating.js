import { Component, ChangeDetectionStrategy, Input, Output, EventEmitter, TemplateRef, ContentChild, forwardRef, ChangeDetectorRef } from '@angular/core';
import { NgbRatingConfig } from './rating-config';
import { toString, getValueInRange } from '../util/util';
import { NG_VALUE_ACCESSOR } from '@angular/forms';
var Key;
(function (Key) {
    Key[Key["End"] = 35] = "End";
    Key[Key["Home"] = 36] = "Home";
    Key[Key["ArrowLeft"] = 37] = "ArrowLeft";
    Key[Key["ArrowUp"] = 38] = "ArrowUp";
    Key[Key["ArrowRight"] = 39] = "ArrowRight";
    Key[Key["ArrowDown"] = 40] = "ArrowDown";
})(Key || (Key = {}));
var NGB_RATING_VALUE_ACCESSOR = {
    provide: NG_VALUE_ACCESSOR,
    useExisting: forwardRef(function () { return NgbRating; }),
    multi: true
};
/**
 * Rating directive that will take care of visualising a star rating bar.
 */
var NgbRating = (function () {
    function NgbRating(config, _changeDetectorRef) {
        this._changeDetectorRef = _changeDetectorRef;
        this.contexts = [];
        this.disabled = false;
        /**
         * An event fired when a user is hovering over a given rating.
         * Event's payload equals to the rating being hovered over.
         */
        this.hover = new EventEmitter();
        /**
         * An event fired when a user stops hovering over a given rating.
         * Event's payload equals to the rating of the last item being hovered over.
         */
        this.leave = new EventEmitter();
        /**
         * An event fired when a user selects a new rating.
         * Event's payload equals to the newly selected rating.
         */
        this.rateChange = new EventEmitter(true);
        this.onChange = function (_) { };
        this.onTouched = function () { };
        this.max = config.max;
        this.readonly = config.readonly;
    }
    NgbRating.prototype.ariaValueText = function () { return this.nextRate + " out of " + this.max; };
    NgbRating.prototype.enter = function (value) {
        if (!this.readonly && !this.disabled) {
            this._updateState(value);
        }
        this.hover.emit(value);
    };
    NgbRating.prototype.handleBlur = function () { this.onTouched(); };
    NgbRating.prototype.handleClick = function (value) { this.update(this.resettable && this.rate === value ? 0 : value); };
    NgbRating.prototype.handleKeyDown = function (event) {
        if (Key[toString(event.which)]) {
            event.preventDefault();
            switch (event.which) {
                case Key.ArrowDown:
                case Key.ArrowLeft:
                    this.update(this.rate - 1);
                    break;
                case Key.ArrowUp:
                case Key.ArrowRight:
                    this.update(this.rate + 1);
                    break;
                case Key.Home:
                    this.update(0);
                    break;
                case Key.End:
                    this.update(this.max);
                    break;
            }
        }
    };
    NgbRating.prototype.ngOnChanges = function (changes) {
        if (changes['rate']) {
            this.update(this.rate);
        }
    };
    NgbRating.prototype.ngOnInit = function () {
        this.contexts = Array.from({ length: this.max }, function () { return ({ fill: 0 }); });
        this._updateState(this.rate);
    };
    NgbRating.prototype.registerOnChange = function (fn) { this.onChange = fn; };
    NgbRating.prototype.registerOnTouched = function (fn) { this.onTouched = fn; };
    NgbRating.prototype.reset = function () {
        this.leave.emit(this.nextRate);
        this._updateState(this.rate);
    };
    NgbRating.prototype.setDisabledState = function (isDisabled) { this.disabled = isDisabled; };
    NgbRating.prototype.update = function (value, internalChange) {
        if (internalChange === void 0) { internalChange = true; }
        var newRate = getValueInRange(value, this.max, 0);
        if (!this.readonly && !this.disabled && this.rate !== newRate) {
            this.rate = newRate;
            this.rateChange.emit(this.rate);
        }
        if (internalChange) {
            this.onChange(this.rate);
            this.onTouched();
        }
        this._updateState(this.rate);
    };
    NgbRating.prototype.writeValue = function (value) {
        this.update(value, false);
        this._changeDetectorRef.markForCheck();
    };
    NgbRating.prototype._getFillValue = function (index) {
        var diff = this.nextRate - index;
        if (diff >= 1) {
            return 100;
        }
        if (diff < 1 && diff > 0) {
            return Number.parseInt((diff * 100).toFixed(2));
        }
        return 0;
    };
    NgbRating.prototype._updateState = function (nextValue) {
        var _this = this;
        this.nextRate = nextValue;
        this.contexts.forEach(function (context, index) { return context.fill = _this._getFillValue(index); });
    };
    return NgbRating;
}());
export { NgbRating };
NgbRating.decorators = [
    { type: Component, args: [{
                selector: 'ngb-rating',
                changeDetection: ChangeDetectionStrategy.OnPush,
                host: {
                    'class': 'd-inline-flex',
                    'tabindex': '0',
                    'role': 'slider',
                    'aria-valuemin': '0',
                    '[attr.aria-valuemax]': 'max',
                    '[attr.aria-valuenow]': 'nextRate',
                    '[attr.aria-valuetext]': 'ariaValueText()',
                    '[attr.aria-disabled]': 'readonly ? true : null',
                    '(blur)': 'handleBlur()',
                    '(keydown)': 'handleKeyDown($event)',
                    '(mouseleave)': 'reset()'
                },
                template: "\n    <ng-template #t let-fill=\"fill\">{{ fill === 100 ? '&#9733;' : '&#9734;' }}</ng-template>\n    <ng-template ngFor [ngForOf]=\"contexts\" let-index=\"index\">\n      <span class=\"sr-only\">({{ index < nextRate ? '*' : ' ' }})</span>\n      <span (mouseenter)=\"enter(index + 1)\" (click)=\"handleClick(index + 1)\" [style.cursor]=\"readonly || disabled ? 'default' : 'pointer'\">\n        <ng-template [ngTemplateOutlet]=\"starTemplate || t\" [ngOutletContext]=\"contexts[index]\"></ng-template>\n      </span>\n    </ng-template>\n  ",
                providers: [NGB_RATING_VALUE_ACCESSOR]
            },] },
];
/** @nocollapse */
NgbRating.ctorParameters = function () { return [
    { type: NgbRatingConfig, },
    { type: ChangeDetectorRef, },
]; };
NgbRating.propDecorators = {
    'max': [{ type: Input },],
    'rate': [{ type: Input },],
    'readonly': [{ type: Input },],
    'resettable': [{ type: Input },],
    'starTemplate': [{ type: Input }, { type: ContentChild, args: [TemplateRef,] },],
    'hover': [{ type: Output },],
    'leave': [{ type: Output },],
    'rateChange': [{ type: Output },],
};
//# sourceMappingURL=rating.js.map