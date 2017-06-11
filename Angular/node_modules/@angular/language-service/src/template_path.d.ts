/**
 * @license
 * Copyright Google Inc. All Rights Reserved.
 *
 * Use of this source code is governed by an MIT-style license that can be
 * found in the LICENSE file at https://angular.io/license
 */
import { AttrAst, BoundDirectivePropertyAst, BoundElementPropertyAst, BoundEventAst, BoundTextAst, DirectiveAst, ElementAst, EmbeddedTemplateAst, NgContentAst, ReferenceAst, TemplateAst, TemplateAstVisitor, TextAst, VariableAst } from '@angular/compiler';
import { AstPath } from './ast_path';
export declare class TemplateAstPath extends AstPath<TemplateAst> {
    position: number;
    constructor(ast: TemplateAst[], position: number, allowWidening?: boolean);
}
export declare class NullTemplateVisitor implements TemplateAstVisitor {
    visitNgContent(ast: NgContentAst): void;
    visitEmbeddedTemplate(ast: EmbeddedTemplateAst): void;
    visitElement(ast: ElementAst): void;
    visitReference(ast: ReferenceAst): void;
    visitVariable(ast: VariableAst): void;
    visitEvent(ast: BoundEventAst): void;
    visitElementProperty(ast: BoundElementPropertyAst): void;
    visitAttr(ast: AttrAst): void;
    visitBoundText(ast: BoundTextAst): void;
    visitText(ast: TextAst): void;
    visitDirective(ast: DirectiveAst): void;
    visitDirectiveProperty(ast: BoundDirectivePropertyAst): void;
}
export declare class TemplateAstChildVisitor implements TemplateAstVisitor {
    private visitor;
    constructor(visitor?: TemplateAstVisitor);
    visitEmbeddedTemplate(ast: EmbeddedTemplateAst, context: any): any;
    visitElement(ast: ElementAst, context: any): any;
    visitDirective(ast: DirectiveAst, context: any): any;
    visitNgContent(ast: NgContentAst, context: any): any;
    visitReference(ast: ReferenceAst, context: any): any;
    visitVariable(ast: VariableAst, context: any): any;
    visitEvent(ast: BoundEventAst, context: any): any;
    visitElementProperty(ast: BoundElementPropertyAst, context: any): any;
    visitAttr(ast: AttrAst, context: any): any;
    visitBoundText(ast: BoundTextAst, context: any): any;
    visitText(ast: TextAst, context: any): any;
    visitDirectiveProperty(ast: BoundDirectivePropertyAst, context: any): any;
    protected visitChildren<T extends TemplateAst>(context: any, cb: (visit: (<V extends TemplateAst>(children: V[] | undefined) => void)) => void): any;
}
