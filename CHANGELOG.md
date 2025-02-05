# Change Log

This document records all notable changes to [Converter CSV by LimberDuck][1].

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.1] - 2025-02-05

### Changed

- code formatted with [black](https://black.readthedocs.io)
- requirements update
  - from:
    - chardet>=4.0.0
    - imageio>=2.9.0
    - PyQt5>=5.15.4
    - XlsxWriter>=3.0.1
  - to:
    - chardet>=5.2.0
    - imageio>=2.37.0
    - PyQt5>=5.15.11
    - XlsxWriter>=3.2.2
- tests for python
  - added: 3.10, 3.11, 3.12, 3.13
  - removed: 3.6, 3.7

## [0.3.0] - 2021-08-30

### Added

- `converter-csv` as Python package - from now on you can install it with `pip install converter-csv`
- entry point `converter-csv` added - from now on, after installation of **Converter CSV** you can run it with command `converter-csv`


## [0.2.3] - 2021-03-27

### Changed

- Requirements updated with new version of pillow and pyinstaller.

## [0.2.2] - 2019-05-18

### Changed

- Suffix with timestamp changed to format displayed in gui.

## [0.2.1] - 2019-05-18

### Changed

- Cancel option handled if change target directory action has been taken.
- About dialog window format changed to display release date.


## [0.2.0] - 2019-05-12

### Added

- possibility to add suffix to output files with current time or/and custom text

## [0.1.0] - 2018-12-31

- Initial public release

[0.3.1]: https://github.com/LimberDuck/converter-csv/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/LimberDuck/converter-csv/compare/v0.2.3...v0.3.0
[0.2.3]: https://github.com/LimberDuck/converter-csv/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/LimberDuck/converter-csv/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/LimberDuck/converter-csv/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/LimberDuck/converter-csv/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/LimberDuck/converter-csv/releases/tag/v0.1.0

[1]: https://github.com/LimberDuck/converter-csv