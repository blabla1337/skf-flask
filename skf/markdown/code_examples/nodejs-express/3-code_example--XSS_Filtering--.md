# XSS filtering
-------

## Example:
	/* If you're creating server - side pages you can use dompurify to sanitize strings like so */
	var clean = DOMPurify.sanitize(dirty);
	//then you can use clean as normal

	/* If you're using a template engine, then AVOID using the following methods */

	/* Mustache js */
	{{{raw html }}}

	/* Handlebars */
	{{{ raw html }}}

	/* e js */
	<%- raw html %>

	/* nunjucks */
	{% raw html %}

	/* angular */
	<h1 ng-bind-html="data.text"></h1>

	/* react js */
	<div dangerouslySetInnerHTML={someFunction()} />
	
	/* @TODO: add more frameworks*/