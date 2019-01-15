from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='paraphs',
    version='1.0.0',
    description='Creates graphical ornamets by parsing texts.',
    url='https://motform.org',
    author='motform',
    author_email='arkiv@motform.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Multimedia',
        'LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 OR LATER (GPLV3+)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # You can just specify package directories manually here if your project is
    # simple. Or you can use find_packages().
    #
    # Alternatively, if you just want to distribute a single Python file, use
    # the `py_modules` argument instead as follows, which will expect a file
    # called `my_module.py` to exist:
    #
    #   py_modules=["my_module"],
    #
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    entry_points={  # Optional
        'console_scripts': [
            'paraphs=paraphs.__init__:main',
        ],
    },
)
