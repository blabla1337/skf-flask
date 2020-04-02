
import unittest

from .test_skf import TestRestPlusApi, TestSecurity


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRestPlusApi))
    suite.addTest(unittest.makeSuite(TestSecurity))

    return suite
