import os
from setuptools import setup, find_packages

this_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_dir, 'README.md'), 'r') as f:
    long_description = f.read()

setup(name='boa',
      version='0.1',
      author='Bounouar Colin',
      maintainer='Bounouar Colin',
      url='https://github.com/Colin-b/pyconfigparser',
      description='Helper to parse configuration files.',
      long_description=long_description,
      download_url='https://github.com/Colin-b/pyconfigparser',
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers"
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Operating System :: Microsoft :: Windows :: Windows 7"
      ],
      keywords=[
          'configuration'
      ],
      packages=find_packages(),
      install_requires=[
      ],
      platforms=[
          'Windows'
      ]
      )
