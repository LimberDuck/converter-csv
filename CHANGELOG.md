# Change Log

This document records all notable changes to [Converter CSV by LimberDuck][1].

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.6.0] - 2025-11-26

### Added

- **Auto-detect separator** - Separators such as `,`, `;`, `tab`, `|` and `:` are automatically detected based on the first 5 lines. This option is enabled by default. Disable it to set the separator manually.
- **Drag & drop** - now you can drag and drop selected files or directories on *Converter CSV by LimberDuck* window to open csv files faster.
 
## [0.5.0] - 2025-10-09

### Added

- **Announcements** visible in Progress Preview window. Displayed just after opening or by selecting `Help > Check Announcements`.
 
### Changed

- **Check for Update** will notify automatically if new version is available just after opening.
- Progress Preview window with font colors suited to light and dark mode
- Option suffix with date enabled by default.
- **Validation of user input for custom suffix** - Settings > Target files > add custom suffix - now you will not be able to put chars like `\` `/` `:` `*` `?` `"` `<` `>` `|` which will let you save target file without any problem.
- Requirements update
  - new:
    - packaging>=25.0

## [0.4.3] - 2025-09-08

### Changed

- Just a pipeline triggers test.

## [0.4.2] - 2025-09-08

### Changed

- Suffix label width increased to improve GUI on Windows.

## [0.4.1] - 2025-09-08

### Added

- Pipeline with Build and Release for Windows, macOS and Linux.
- Requirements update
  - new:
    - requests>=2.32.5

### Changed

- Icon file changed and renamed from `LimberDuck-converter-csv` to `LimberDuck-Converter-CSV`.
- Default target directory changed from *current directory* to *user’s home directory*.
- Fix for app build on macOS.
- Update check directing to GitHub Releases as well.
- Suffix fields width increased to improve GUI on Windows.
- `version.rc` file info updated.

## [0.4.0] - 2025-09-01

### Added

- New options:
  - `Help > Check for Update` - will return confirmation if you are using the latest version of Converter CSV.
  - `Help > Documentation` - will open Converter CSV documentation at LimberDuck.org.
  - `Help > GitHub` - will open Converter CSV GitHub page.
  - `Help > Releases` - will open Converter CSV GitHub Releases page.

### Changed

- Requirements update
  - from:
    - XlsxWriter>=3.2.2
  - to:
    - XlsxWriter>=3.2.5
  - new:
    - packaging>=25.0

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
  - removed: 3.6, 3.7, 3.8, 3.9, 3.10

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

[0.4.3]: https://github.com/LimberDuck/converter-csv/compare/v0.4.2...v0.4.3
[0.4.2]: https://github.com/LimberDuck/converter-csv/compare/v0.4.1...v0.4.2
[0.4.1]: https://github.com/LimberDuck/converter-csv/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/LimberDuck/converter-csv/compare/v0.3.1...v0.4.0
[0.3.1]: https://github.com/LimberDuck/converter-csv/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/LimberDuck/converter-csv/compare/v0.2.3...v0.3.0
[0.2.3]: https://github.com/LimberDuck/converter-csv/compare/v0.2.2...v0.2.3
[0.2.2]: https://github.com/LimberDuck/converter-csv/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/LimberDuck/converter-csv/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/LimberDuck/converter-csv/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/LimberDuck/converter-csv/releases/tag/v0.1.0

[1]: https://github.com/LimberDuck/converter-csv