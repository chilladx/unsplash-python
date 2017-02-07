from setuptools import setup

setup(
    name='unsplash-python',
    version='1.0.0a1',
    packages=['unsplash', 'unsplash.src'],
    description='A unofficial Python wrapper for the Unsplash API',
    url='https://github.com/michael-hacker/unsplash-python/',
    license='MIT',
    author='Michael Hacker',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5'
    ],
    keywords=['unsplash', 'api', 'python'],
    install_requires=['requests']
)