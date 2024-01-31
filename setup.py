from setuptools import find_namespace_packages, setup


DESCRIPTION = 'Python client library for the LMNT API'
AUTHOR = 'LMNT, Inc.'
AUTHOR_EMAIL = 'feedback@lmnt.com'
URL = 'https://github.com/lmnt-com/lmnt-python'
LICENSE = 'Apache 2.0'
KEYWORDS = ['speech tts ai ml genai']
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
]

setup(name='lmnt',
      description=DESCRIPTION,
      long_description=open('README.md', 'r').read(),
      long_description_content_type='text/markdown',
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      license=LICENSE,
      keywords=KEYWORDS,
      packages=find_namespace_packages('src'),
      package_dir={'': 'src'},
      install_requires=[
          'aiohttp ~= 3.8'
      ],
      classifiers=CLASSIFIERS)
