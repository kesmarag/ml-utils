from setuptools import setup

setup(name='kesmarag-ml-utils',
      version='0.0.1',
      description='Machine learning utilities',
      author='Costas Smaragdakis',
      author_email='kesmarag@gmail.com',
      url='https://github.com/kesmarag/ml-utils',
      packages=['kesmarag.ml.utils'],
      package_dir={'kesmarag.ml.utils': './'},
      install_requires=['numpy>=1.12.1'], )
