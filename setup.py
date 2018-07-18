from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pandas_multiprocess',
    version='0.0.1',
    author='Qihui Xie',
    author_email='xieqihui@gmail.com',
    maintainer='Qihui Xie',
    maintainer_email='xieqihui@gmail.com',
    url='https://github.com/xieqihui/pandas_multiprocess.git',
    license="LICENSE.txt",
    description='Multiprocessing Support for Pandas DataFramed',
    long_description='Multiprocessing Support for Pandas DataFramed',
    packages=['pandas_multiprocess'],
    install_requires=required
)
