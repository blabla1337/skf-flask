try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='skf',
    version='1.3.21',
    description='The OWASP Security Knowledge Framework',
    url='https://github.com/blabla1337/skf-flask',
    author='Glenn ten Cate, Riccardo ten Cate',
    author_email='glenn.ten.cate@owasp.org, riccardo.ten.cate@owasp.org',
    license='AGPLV3',
    packages=['skf'],
    include_package_data = True,
    long_description="""\
    The Security Knowledge Framework is an fully open-source Python Flask API.
    It is an expert system application that uses OWASP Application Security Verification Standard and helps developers to do security by design.
    """,
    install_requires=required,
    test_suite='tests.suite',
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
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ]
)
