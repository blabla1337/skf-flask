import { Directive, Input } from '@angular/core';
/**
 * The NgbCollapse directive provides a simple way to hide and show an element with animations.
 */
var NgbCollapse = (function () {
    function NgbCollapse() {
        /**
         * A flag indicating collapsed (true) or open (false) state.
         */
        this.collapsed = false;
    }
    return NgbCollapse;
}());
export { NgbCollapse };
NgbCollapse.decorators = [
    { type: Directive, args: [{
                selector: '[ngbCollapse]',
                exportAs: 'ngbCollapse',
                host: { '[class.collapse]': 'true', '[class.show]': '!collapsed' }
            },] },
];
/** @nocollapse */
NgbCollapse.ctorParameters = function () { return []; };
NgbCollapse.propDecorators = {
    'collapsed': [{ type: Input, args: ['ngbCollapse',] },],
};
//# sourceMappingURL=collapse.js.map