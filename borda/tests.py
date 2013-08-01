"""
Module: tests.py

This module holds all tests for the borda application

Author: Luis Osa <luis.osa.gdc@gmail.com>
"""
import doctest


def test_suite():
    """Return all doctests as a test suite, required by zope.testrunner"""
    return doctest.DocFileSuite(
        '../README.rst',
        'server.rst',
        'client.rst',
        optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
