"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var HighlightJsContentDirective = (function () {
    function HighlightJsContentDirective(elementRef, zone) {
        this.elementRef = elementRef;
        this.zone = zone;
    }
    HighlightJsContentDirective.prototype.ngOnInit = function () {
        if (this.useBr) {
            hljs.configure({ useBR: true });
        }
    };
    HighlightJsContentDirective.prototype.ngAfterViewChecked = function () {
        var selector = this.highlightSelector || 'code';
        if (this.elementRef.nativeElement.innerHTML && this.elementRef.nativeElement.querySelector) {
            var snippets_1 = this.elementRef.nativeElement.querySelectorAll(selector);
            this.zone.runOutsideAngular(function () {
                for (var _i = 0, snippets_2 = snippets_1; _i < snippets_2.length; _i++) {
                    var snippet = snippets_2[_i];
                    hljs.highlightBlock(snippet);
                }
            });
        }
    };
    return HighlightJsContentDirective;
}());
HighlightJsContentDirective.decorators = [
    { type: core_1.Directive, args: [{
                selector: '[highlight-js-content]'
            },] },
];
/** @nocollapse */
HighlightJsContentDirective.ctorParameters = function () { return [
    { type: core_1.ElementRef, },
    { type: core_1.NgZone, },
]; };
HighlightJsContentDirective.propDecorators = {
    'useBr': [{ type: core_1.Input },],
    'highlightSelector': [{ type: core_1.Input, args: ['highlight-js-content',] },],
};
exports.HighlightJsContentDirective = HighlightJsContentDirective;
//# sourceMappingURL=highlight-js-content.directive.js.map