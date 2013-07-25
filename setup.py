from setuptools import setup

setup(name='borda',
      version='0.0.1',
      install_requires=[
          'bottle',
          'requests'],
      entry_points={
          'console_scripts': [
          'bordad=borda.server.main:run',
          'borda=borda.client.main:run']})
