/**
 * @license
 * Copyright Google Inc. All Rights Reserved.
 *
 * Use of this source code is governed by an MIT-style license that can be
 * found in the LICENSE file at https://angular.io/license
 */
import { AngularCompilerOptions, CompilerHost } from '@angular/compiler-cli';
import * as ts from 'typescript';
export declare class ReflectorHost extends CompilerHost {
    private getProgram;
    constructor(getProgram: () => ts.Program, serviceHost: ts.LanguageServiceHost, options: AngularCompilerOptions);
    protected program: ts.Program;
}
