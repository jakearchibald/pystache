# encoding: utf-8

"""
This module contains the initialization logic called by __init__.py.

"""

from .template import Template
from .view import View
from .loader import Loader


__all__ = ['Template', 'View', 'Loader', 'render']


def render(template, context=None, **kwargs):
    """
    Return the given template string rendered using the given context.

    """
    return Template(template, context, **kwargs).render()