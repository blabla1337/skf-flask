import sys
import unittest


try:
    from coverage import coverage
    coverage_available = True
except ImportError:
    coverage_available = False


def run():
    if coverage_available:
        cov = coverage(source=['skf'])
        cov.start()

    from tests import suite
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    if not result.wasSuccessful():
        sys.exit(1)

    if coverage_available:
        cov.stop()
        print("\nCode Coverage")
        cov.report()
        cov.html_report(directory='cover')
    else:
        print("\nTipp:\n\tUse 'pip install coverage' to get great code "
              "coverage stats")

if __name__ == '__main__':
    run()

