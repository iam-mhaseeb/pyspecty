import  io
from setuptools import setup

with io.open('README.md', encoding='utf_8') as fp:
    readme = fp.read()

setup(name='pywordcloudy',
      version='1.1',
      description='A happy light weight library to search python errors on stackoverflow automatically.',
      long_description=readme,
      long_description_content_type='text/markdown',
      keywords='python, errors, debugging',
      url='https://github.com/iam-mhaseeb/pyspecty',
      author='Muhammad Haseeb',
      author_email='haseeb.emailbox@gmail.com',
      license='MIT',
      packages=['pyspecty'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
