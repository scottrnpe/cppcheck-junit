from setuptools import setup

setup(
    name="cppcheck-junit",
    version="2.2.0",
    description="Converts Cppcheck XML output to JUnit format.",
    long_description=open("README.rst").read(),
    keywords="Cppcheck C++ JUnit",
    author="John Hagen",
    author_email="johnthagen@gmail.com",
    url="https://github.com/johnthagen/cppcheck-junit",
    py_modules=["cppcheck_junit"],
    install_requires=open("requirements.txt").readlines(),
    python_requires=">=3.7",
    zip_safe=False,
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: C++",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Quality Assurance",
    ],
    scripts=["cppcheck_junit.py"],
    entry_points={
        "console_scripts": [
            "cppcheck_junit = cppcheck_junit:main",
        ],
    },
)
