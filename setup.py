from distutils.core import setup
requires = ['mpmath']
setup(
        name = "lunisolar",
        packages = ["lunisolar", "pycalcal"],
        install_requires=requires,
        version = "0.1.3",
        description = "A library to handle the Chinese calendar",
        long_description=open('README.rst').read(),
        author = "Lee Wei Yen",
        author_email = "lee@weiyen.me",
        url = "https://github.com/yen223/lunisolar",
        classifiers = [
            "Programming Language :: Python",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Libraries",
            "Topic :: Utilities",
            "Topic :: Sociology",
            "Topic :: Software Development :: Internationalization"
            ]
        )
