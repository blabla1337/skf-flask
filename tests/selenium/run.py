import sys
import unittest


try:
    from selenium import webdriver
    selenium_available = True
except ImportError:
    selenium_available = False


from tests.selenium import suite
result = unittest.TextTestRunner(verbosity=2).run(suite())
if not result.wasSuccessful():
    sys.exit(1)
else:
    print(result)

if selenium_available:
    print("\nCode End to End testing with Selenium")
else:
    print("\nTipp:\n\tUse 'pip3 install selenium' to get great code ")


