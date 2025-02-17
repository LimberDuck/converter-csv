import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

about = {}
with open("converter_csv/_version.py") as f:
    exec(f.read(), about)

setuptools.setup(
    name="converter_csv",
    version=about["__version__"],
    license="GPLv3",
    author="Damian Krawczyk",
    author_email="damian.krawczyk@limberduck.org",
    description="Converter CSV by LimberDuck is a GUI tool to convert multiple large csv files to xlsx files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LimberDuck/converter-csv",
    packages=setuptools.find_packages(),
    install_requires=required,
    entry_points={"gui_scripts": ["converter-csv = converter_csv.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: X11 Applications :: Qt",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
    ],
)
