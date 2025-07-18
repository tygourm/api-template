# Release Engineering

Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

Additional labels for pre-release and build metadata are available as extensions
to the MAJOR.MINOR.PATCH format.

From `develop` branch for a major or minor release, or `master` for a patch:

- `git checkout -b release/x.y.z`, last checks, lint, format and tests
- Update the references to the current version in the sources
- Update the lock file with `uv sync --all-groups`
- Update the [Changelog](CHANGELOG.md), set the new version with the release
  date
- Commit as `🔖 Version x.y.z`, create a release from the branch with a tag, and
  the content of the [Changelog](CHANGELOG.md)
- Merge branch `release/x.y.z` into `master` and `develop`
