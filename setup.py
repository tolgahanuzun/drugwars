from setuptools import setup

setup(
    packages=['drugwars'],
    name = 'drugwars cli',
    version = '0.0.1',
    author='Tolgahan Üzün',
    author_email='mail@tolgahanuzun.com',
    url='https://github.com/tolgahanuzun/drugwars',
    entry_points={
        'console_scripts': [
            'drugwars = drugwars.app:main',
        ],
    },
    install_requires=[
        'steem',
    ],
)