import uuid

from pip.req import parse_requirements
from setuptools import setup, find_packages

install_requirements = parse_requirements('requirements.txt', session=uuid.uuid1())
requirements = [str(req.req) for req in install_requirements]

setup(
    name='unsplash-python',
    version='1.0.0a6',
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
        'Programming Language :: Python :: 3.5'
    ],
    keywords='api development unsplash',
    install_requires=requirements,
    zip_safe=True
)