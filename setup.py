# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('LICENSE') as f:
    license = f.read()

filename = "%s/version.py" % 'skf'
with open(filename) as f:
        exec(f.read())

setup(name='owasp-skf',
    version=__version__,
    description='The OWASP Security Knowledge Framework',
    url='https://github.com/blabla1337/skf-flask',
    author='Glenn ten Cate, Riccardo ten Cate',
    author_email='glenn.ten.cate@owasp.org, riccardo.ten.cate@owasp.org',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    # trying to add files...
    include_package_data = True,
    long_description="""\
    The Security Knowledge Framework is an fully open-source Python-Flask web-application.
    It is an expert system application that uses OWASP Application Security Verification Standard
    """,
    install_requires=['flask>0.11, <0.12',
                      'markdown==2.6.3',
                      'BeautifulSoup',
                      'python-docx',
                      'lxml==3.4.2',
                      'pyOpenSSL',
                      'requests',
                      'importlib',
                      'flask-bcrypt'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'jsonschema'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flask",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Topic :: Software Development",
        "Topic :: Security",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ])
