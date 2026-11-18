# OSS Maintainer Toolkit

A small, dependency-free Python command-line toolkit for maintaining public open-source repositories. It checks common repository hygiene basics and produces a JSON report that maintainers can review locally.

**Status:** early starter project. It is not affiliated with Anthropic, GitHub, or OpenSSF, and it does not claim to satisfy any programme eligibility threshold.

## Why this exists

Small maintainers often need a repeatable way to check whether a repository has a licence, contribution guide, security policy, code of conduct, changelog, tests, and release notes. This tool provides a transparent, offline checklist so those gaps are visible.

## Requirements

- Python 3.10+
- No third-party runtime dependencies

## Usage

```bash
python -m src.oss_maintainer_toolkit path/to/repository
python -m src.oss_maintainer_toolkit path/to/repository --json report.json
```

The tool only reads repository files. It does not change files, upload code, contact services, or claim that a repository is secure or compliant.

## Checks

- MIT, Apache-2.0, BSD, GPL and other common licence file names
- README, CONTRIBUTING, SECURITY, CODE_OF_CONDUCT and CHANGELOG presence
- GitHub Actions workflow directory presence
- Test directory presence

These are presence checks, not legal, security, CI, or quality certification. A human must verify the contents and applicability.

## Development

```bash
python -m unittest discover -s tests -v
```

## Licence

MIT. Copyright (c) 2026 the project contributors. See [LICENSE](LICENSE).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Real bug reports, tests, documentation and cross-platform improvements are welcome.
