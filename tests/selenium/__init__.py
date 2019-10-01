import unittest
import tests.selenium.e2e_tests
from tests.selenium.e2e_tests import SKFClickThrough

def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SKFClickThrough))
    return suite