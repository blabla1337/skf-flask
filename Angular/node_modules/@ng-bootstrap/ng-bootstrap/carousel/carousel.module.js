import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { NGB_CAROUSEL_DIRECTIVES } from './carousel';
import { NgbCarouselConfig } from './carousel-config';
export { NgbCarousel, NgbSlide } from './carousel';
export { NgbCarouselConfig } from './carousel-config';
var NgbCarouselModule = (function () {
    function NgbCarouselModule() {
    }
    NgbCarouselModule.forRoot = function () { return { ngModule: NgbCarouselModule, providers: [NgbCarouselConfig] }; };
    return NgbCarouselModule;
}());
export { NgbCarouselModule };
NgbCarouselModule.decorators = [
    { type: NgModule, args: [{ declarations: NGB_CAROUSEL_DIRECTIVES, exports: NGB_CAROUSEL_DIRECTIVES, imports: [CommonModule] },] },
];
/** @nocollapse */
NgbCarouselModule.ctorParameters = function () { return []; };
//# sourceMappingURL=carousel.module.js.map