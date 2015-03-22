try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='owasp-skf',
    version='0.2.8a4',
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
        'git+https://github.com/mitsuhiko/flask.git#egg=Flask-owasp'
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Flask",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ])


