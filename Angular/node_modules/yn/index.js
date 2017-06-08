'use strict';
var lenient = require('./lenient');

module.exports = function (val, opts) {
	val = String(val).trim();
	opts = opts || {};

	if (/^(?:y|yes|true|1)$/i.test(val)) {
		return true;
	}

	if (/^(?:n|no|false|0)$/i.test(val)) {
		return false;
	}

	if (opts.lenient === true) {
		return lenient(val);
	}

	return null;
};
