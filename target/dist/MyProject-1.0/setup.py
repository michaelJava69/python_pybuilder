#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'MyProject',
        version = '1.0',
        description = 'Example PyBuilder / Git project',
        long_description = 'An example PyBuilder / Git project for project management\nand file version control. See blog post at http://bit.ly/2QY65wO for a\nmore through explanation.',
        author = 'Michael Ugbechie',
        author_email = 'michael.named@gmail.com',
        license = 'None',
        url = 'https://github.com/awwsmm/PybGit',
        scripts = ['scripts/example_hello_script.py'],
        packages = [],
        namespace_packages = [],
        py_modules = [
            'example_hello',
            'example_primes'
        ],
        classifiers = [
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python'
        ],
        entry_points = {},
        data_files = [],
        package_data = {},
        install_requires = [],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '',
        obsoletes = [],
    )
