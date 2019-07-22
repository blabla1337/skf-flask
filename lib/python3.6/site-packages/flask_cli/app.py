# -*- coding: utf-8 -*-
"""
    flask.app
    ~~~~~~~~~

    This module implements the central WSGI application object.

    :copyright: (c) 2015 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""

from functools import update_wrapper

from flask.globals import g


def setupmethod(f):
    """Wraps a method so that it performs a check in debug mode if the
    first request was already handled.
    """
    def wrapper_func(self, *args, **kwargs):
        if self.debug and self._got_first_request:
            raise AssertionError('A setup function was called after the '
                'first request was handled.  This usually indicates a bug '
                'in the application where a module was not imported '
                'and decorators or other functionality was called too late.\n'
                'To fix this make sure to import all your view modules, '
                'database models and everything related at a central place '
                'before the application starts serving requests.')
        return f(self, *args, **kwargs)
    return update_wrapper(wrapper_func, f)


def make_shell_context(self):
    """Returns the shell context for an interactive shell for this
    application.  This runs all the registered shell context
    processors.

    .. versionadded:: 1.0
    """
    rv = {'app': self, 'g': g}
    for processor in self.shell_context_processors:
        rv.update(processor())
    return rv

@setupmethod
def shell_context_processor(self, f):
    """Registers a shell context processor function.

    .. versionadded:: 1.0
    """
    self.shell_context_processors.append(f)
    return f
