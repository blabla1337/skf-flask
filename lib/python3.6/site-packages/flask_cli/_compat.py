# -*- coding: utf-8 -*-
"""
    flask._compat
    ~~~~~~~~~~~~~

    Some py2/py3 compatibility support based on a stripped down
    version of six so we don't have to depend on a specific version
    of it.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
import sys

PY2 = sys.version_info[0] == 2
_identity = lambda x: x


if not PY2:
    iteritems = lambda d: iter(d.items())

    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value
else:
    iteritems = lambda d: d.iteritems()
    exec('def reraise(tp, value, tb=None):\n raise tp, value, tb')
