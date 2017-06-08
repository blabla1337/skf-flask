"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var core_1 = require("@angular/core");
var highlight_js_content_directive_1 = require("./highlight-js-content.directive");
var HighlightJsModule = (function () {
    function HighlightJsModule() {
    }
    return HighlightJsModule;
}());
HighlightJsModule.decorators = [
    { type: core_1.NgModule, args: [{
                imports: [],
                providers: [],
                declarations: [
                    highlight_js_content_directive_1.HighlightJsContentDirective
                ],
                exports: [
                    highlight_js_content_directive_1.HighlightJsContentDirective
                ]
            },] },
];
/** @nocollapse */
HighlightJsModule.ctorParameters = function () { return []; };
exports.HighlightJsModule = HighlightJsModule;
var highlight_js_service_1 = require("./highlight-js.service");
exports.HighlightJsService = highlight_js_service_1.HighlightJsService;
//# sourceMappingURL=highlight-js.module.js.map