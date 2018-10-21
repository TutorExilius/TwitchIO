# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2017-2018 TwitchIO

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import re
import subprocess

import setuptools


with open('twitchio/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('TwitchIO version is not set.')

# Thanks Danny(Rapptz) again...
if version.endswith(('a', 'b', 'rc')):
    try:
        # append version identifier based on commit count
        p = subprocess.Popen(
            ['git', 'rev-list', '--count', 'HEAD'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        out, err = p.communicate()
        if out:
            version += out.decode('utf-8').strip()

        p = subprocess.Popen(
            ['git', 'rev-parse', '--short', 'HEAD'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        out, err = p.communicate()
        if out:
            version += '+' + out.decode('utf-8').strip()
    except Exception:
        pass

with open('README.rst') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

extras_require = {
    'docs': (
        'pygments',
        'sphinx==1.7.4',
        'sphinxcontrib-asyncio',
        'sphinxcontrib-napoleon',
        'sphinxcontrib-websupport',
    ),
    'server': (
        'sanic',
    ),
}

setuptools.setup(
    name='twitchio',
    author='TwitchIO',
    url='https://github.com/TwitchIO/TwitchIO',
    version=version,
    packages=['twitchio', 'twitchio.ext.commands', 'twitchio.ext.server'],
    license='MIT',
    description='A Python API and IRC wrapper for Twitch.',
    long_description=readme,
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=requirements,
    extras_require=extras_require,
    classifiers=[
        'Development Status :: 2 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
