from setuptools import setup

setup(name='borda',
      version='0.1',
      packages=['borda'],
      install_requires=[
          'bottle',
          'requests'],
      extras_require={
          'test': ['MiniMock']},
      entry_points={
          'console_scripts': [
          'bordad=borda.server:main',
          'borda=borda.client:run']},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: Bottle',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Topic :: Office/Business :: Groupware'])
