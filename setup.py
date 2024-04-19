# setup.py
from setuptools import setup, find_packages

setup(
    name='python-gmail',
    author='Zack Plauche',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-dotenv',
        'pydantic',
    ],
    entry_points={
        'console_scripts': [
            'my_script=my_package.my_script:main',
        ],
    },
)
