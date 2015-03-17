try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

setup(name='owasp-flask-skf',
      version='0.2.0a2',
      description='The OWASP Security Knowledge Framework',
      url='https://github.com/blabla1337/skf-flask',
      author='Glenn ten Cate, Riccardo ten Cate',
      author_email='gtencate@schubergphilis.com, r.tencate77@gmail.com',
      license='AGPLV3',
      packages=['skf'],
      long_description="""\
      The Security Knowledge Framework is an fully open-source Python-Flask web-application.
      It is an expert system application that uses OWASP Application Security Verification Standard 
      """,
      install_requires=open('requirements.txt').read().splitlines(),
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Framework :: Flask",
          "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
      ])

