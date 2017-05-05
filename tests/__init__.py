
import unittest

from .test_skf import TestRestPlusApi


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRestPlusApi))

    return suite
