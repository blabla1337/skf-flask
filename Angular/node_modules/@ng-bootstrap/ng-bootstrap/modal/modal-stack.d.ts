import { ApplicationRef, Injector, ComponentFactoryResolver } from '@angular/core';
import { NgbModalRef } from './modal-ref';
export declare class NgbModalStack {
    private _applicationRef;
    private _injector;
    private _componentFactoryResolver;
    private _backdropFactory;
    private _windowFactory;
    constructor(_applicationRef: ApplicationRef, _injector: Injector, _componentFactoryResolver: ComponentFactoryResolver);
    open(moduleCFR: ComponentFactoryResolver, contentInjector: Injector, content: any, options: any): NgbModalRef;
    private _applyWindowOptions(windowInstance, options);
    private _getContentRef(moduleCFR, contentInjector, content, context);
}
