import unittest
import uuid

from pip.req import parse_requirements
from setuptools import setup, find_packages

install_requirements = parse_requirements('requirements.txt',
                                          session=uuid.uuid1())
requirements = [str(req.req) for req in install_requirements]


def test_suite():
    test_loader = unittest.defaultTestLoader
    test_suite = test_loader.discover('tests', pattern='test_*.py')

    return test_suite

setup(
    name='unsplash-python',
    version='1.0.0a9',
    packages=['unsplash_python', 'unsplash_python.src'],
    description='A Python wrapper for the Unsplash API',
    url='https://github.com/michael-hacker/unsplash-python',
    license='MIT',
    author='Michael Hacker',
    author_email='mh@superchic.at',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='api development unsplash',
    install_requires=requirements,
    test_suite='setup.test_suite',
    zip_safe=True
)
