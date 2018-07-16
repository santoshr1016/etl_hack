import os
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))
os.chdir(here)
setup(name='ETL_package',
      version='0.1',
      description='The ETL assignment',
      url='https://github.com/santoshr1016/ETL',
      author='R Santosh Kumar',
      author_email='santy.iiitd@gmail.com',
      license='Free',
      packages=['ETL_package'],
      classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development ::  ETL Tools',

        'Programming Language :: Python :: 3.5',
      ],
      zip_safe=False)
