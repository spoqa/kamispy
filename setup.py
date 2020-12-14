import pathlib

from setuptools import find_packages, setup

from kamis import __version__


__all__ = 'readme', 'setup'


def readme() -> str:
    name = pathlib.Path('README.rst')
    try:
        with open(name.resolve(), encoding='utf-8') as f:
            return f.read()
    except (IOError, OSError):
        return


setup(
    name='kamispy',
    version=__version__,
    description='KAMIS Open-API 비공식 파이썬 클라이언트',
    long_description=readme(),
    long_description_content_type='text/x-rst',
    url='https://github.com/spoqa/kamispy',
    license='MIT License',
    author='Spoqa Creators',
    author_emai='dev' '@' 'spoqa.com',
    packages=find_packages(exclude=('tests', 'tests.*')),
    python_requires='>=3.7.0',
    install_requires=['requests'],
    extras_require=dict(
        tests=['flake8', 'pytest', 'requests_mock']
    ),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
