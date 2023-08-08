from os import path

from setuptools import setup, find_packages

current_dir = path.abspath(path.dirname(__file__))
with open(path.join(current_dir, 'README.md')) as f:
    description = f.read()

setup(
    name='nitter',
    packages=find_packages(),
    version='0.0.2',
    license='MIT',
    description='Nitter is a simple library to scrap Twitter data using the Nitter website',
    long_description=description,
    long_description_content_type='text/markdown',
    author='Ali Fotouhi',
    author_email='the.alif.dev@gmail.com ',
    url='https://github.com/iAliF/Nitter/',
    download_url='https://github.com/iAliF/Nitter/archive/refs/tags/v0.0.2-alpha.zip',
    install_requires=['requests', 'beautifulsoup4'],
    keywords=[
        'Nitter', 'Twitter', 'Twitter Scraper'
    ],
    project_urls={
        'Documentation': 'https://github.com/iAliF/Nitter/',
        'Source': 'https://github.com/iAliF/Nitter/',
        'Bug Tracker': 'https://github.com/iAliF/Nitter/issues',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ]
)
