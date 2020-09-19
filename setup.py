from setuptools import setup, find_packages
 
setup(name='coconut',
      version='0.0.1',
      url='https://github.com/imzeki/coconut',
      license='MIT',
      author='Ezekiel Ruazol Gonzales',
      author_email='ezekiel.r.gonzales@gmail.com',
      description='Coconut is a module for simplifying simple things and chunk them down into even simpler tasks',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)