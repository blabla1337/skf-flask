try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='owasp-skf',
    version='0.2.1',
    description='The OWASP Security Knowledge Framework',
    url='https://github.com/blabla1337/skf-flask',
    author='Glenn ten Cate, Riccardo ten Cate',
    author_email='gtencate@schubergphilis.com, r.tencate77@gmail.com',
    license='AGPLV3',
    packages=['skf'],
    # trying to add files...
    include_package_data = True,
    long_description="""\
    The Security Knowledge Framework is an fully open-source Python-Flask web-application.
    It is an expert system application that uses OWASP Application Security Verification Standard
    """,
    install_requires=['markdown','BeautifulSoup','python-docx','pyOpenSSL','Flask-owasp'],
    dependency_links= [
        'https://github.com/mitsuhiko/flask/tarball/master#egg=Flask-owasp'
    ],
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
