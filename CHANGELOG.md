# Changelog

## Upstream Julia Mapping

These mappings describe the upstream Julia release lineage used by each Python
release; they are not runtime dependencies.

| Python release | Upstream Julia release |
| --- | --- |
| [v0.4.0] | [CICOBase.jl v0.3.1][cico-v0.3.1] |
| [v0.3.1] | [LikelihoodProfiler.jl v0.3.1][lp-v0.3.1] |
| [v0.3.0] | [LikelihoodProfiler.jl v0.3.0][lp-v0.3.0] |
| [v0.2.1] | [LikelihoodProfiler.jl v0.2.1][lp-v0.2.1] |

## [v0.4.0] - 2026-05-30

### Added

- Added modern GitHub Actions workflows for tests, package verification, and documentation deployment.
- Added reproducible dependency constraints for CI and local development.
- Added `pyproject.toml` project metadata and optional dependency groups for tests, docs, build, and development.
- Added Sphinx documentation pages for the renamed `cicobase` package.
- Added this changelog.

### Changed

- Renamed the primary package from `likelihoodprofiler` to `cicobase`.
- Kept `likelihoodprofiler` as a compatibility import path for existing code.
- Updated CI and tox coverage for Python 3.10 through 3.14.
- Replaced the old frozen `requirements.txt` with minimal runtime dependency ranges.
- Updated README content for the CICOBase naming, installation flow, badges, and project links.
- Removed generated build and documentation artifacts from version control.

### Removed

- Removed legacy Travis CI and AppVeyor configuration.
- Removed the old `docs/likelihoodprofiler.rst` module page in favor of `docs/cicobase.rst`.

## [v0.3.1] - 2020-01-07

### Changed

- Updated dependency references before merging the development branch.
- Added README notes and links around the published reference material.

### Fixed

- Improved behavior when loss function evaluation fails and added regression tests for those error paths.

### Notes

- The Git tag is `v0.3.1`, but the packaged `setup.py` version at this tag still declares `0.3.0`.

## [v0.3.0] - 2019-10-21

### Added

- Added tests covering loss-function error handling.

### Changed

- Bumped the package metadata version to `0.3.0`.
- Reworked CICO, linear extrapolation, quadratic extrapolation, endpoint, profile, and result-structure internals.
- Updated documentation, badges, and reference links.

## [v0.2.1] - 2019-09-17

### Added

- Initial tagged Python package for practical identifiability analysis and confidence interval evaluation.
- Added core `likelihoodprofiler` routines, tests, documentation, and CI configuration.
- Added Windows/AppVeyor and Travis CI setup used by the early project history.

[v0.4.0]: https://github.com/insysbio/CICOBase.py/compare/v0.3.1...v0.4.0
[v0.3.1]: https://github.com/insysbio/CICOBase.py/releases/tag/v0.3.1
[v0.3.0]: https://github.com/insysbio/CICOBase.py/releases/tag/v0.3.0
[v0.2.1]: https://github.com/insysbio/CICOBase.py/releases/tag/v0.2.1
[cico-v0.3.1]: https://github.com/insysbio/CICOBase.jl/releases/tag/v0.3.1
[lp-v0.3.1]: https://github.com/insysbio/LikelihoodProfiler.jl/releases/tag/v0.3.1
[lp-v0.3.0]: https://github.com/insysbio/LikelihoodProfiler.jl/releases/tag/v0.3.0
[lp-v0.2.1]: https://github.com/insysbio/LikelihoodProfiler.jl/releases/tag/v0.2.1
