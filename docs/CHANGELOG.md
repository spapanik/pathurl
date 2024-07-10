# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to [Semantic Versioning].

## [Unreleased]

### Removed

-   Drop python 3.8 support

## [0.7.0] - 2024-05-03

### Added

-   Allow passing multiple paths in URL.join

## [0.6.0] - 2023-06-29

### Added

-   Add constructors for URL, Path, Query that accept the parts as arguments

### Removed

-   Drop python 3.7 support

## [0.5.0] - 2022-01-19

### Added

-   Allow passing a dict in Query methods for keys that cannot be keyword arguments
-   Allow replacing parts of a URL

### Changed

-   Query is immutable, with a new interface
-   Path is immutable, with a new interface
-   URL is immutable, with a new interface

## [0.4.0] - 2022-01-10

### Removed

-   Remove changelog from the published wheel

## [0.3.0] - 2022-01-05

### Added

-   URL has from_string as an alias to parse, to create new URLs
-   Allow joining paths, and URLs with paths

### Changed

-   URL constructor accept kwargs only

### Removed

-   Remove the default scheme
-   Remove params attribute as it is unused

## [0.2.0] - 2022-01-05

### Added

-   Add python 3.10 support

### Removed

-   Drop python 3.6 support

## [0.1.0] - 2021-05-05

### Added

-   Add a class for a URL

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/spec/v2.0.0.html
[Unreleased]: https://github.com/spapanik/pathurl/compare/v0.7.0...main
[0.7.0]: https://github.com/spapanik/pathurl/compare/v0.6.0...0.7.0
[0.6.0]: https://github.com/spapanik/pathurl/compare/v0.5.0...0.6.0
[0.5.0]: https://github.com/spapanik/pathurl/compare/v0.4.0...0.5.0
[0.4.0]: https://github.com/spapanik/pathurl/compare/v0.3.0...0.4.0
[0.3.0]: https://github.com/spapanik/pathurl/compare/v0.2.0...0.3.0
[0.2.0]: https://github.com/spapanik/pathurl/compare/v0.1.0...0.2.0
[0.1.0]: https://github.com/spapanik/pathurl/releases/tag/v0.1.0
