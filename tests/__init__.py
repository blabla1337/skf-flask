
import unittest

from .test_skf import TestRestPlusApi, TestDB, TestSecurity


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestRestPlusApi))
    suite.addTest(unittest.makeSuite(TestSecurity))
    suite.addTest(unittest.makeSuite(TestDB))

    return suite
