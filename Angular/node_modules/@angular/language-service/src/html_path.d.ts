/**
 * @license
 * Copyright Google Inc. All Rights Reserved.
 *
 * Use of this source code is governed by an MIT-style license that can be
 * found in the LICENSE file at https://angular.io/license
 */
import { Attribute, Comment, Element, Expansion, ExpansionCase, Node, Text, Visitor } from '@angular/compiler';
import { AstPath } from './ast_path';
export declare class HtmlAstPath extends AstPath<Node> {
    position: number;
    constructor(ast: Node[], position: number);
}
export declare class ChildVisitor implements Visitor {
    private visitor;
    constructor(visitor?: Visitor);
    visitElement(ast: Element, context: any): any;
    visitAttribute(ast: Attribute, context: any): any;
    visitText(ast: Text, context: any): any;
    visitComment(ast: Comment, context: any): any;
    visitExpansion(ast: Expansion, context: any): any;
    visitExpansionCase(ast: ExpansionCase, context: any): any;
    private visitChildren<T>(context, cb);
}
