# Changelog

All notable changes to this project will be documented here.

## [0.1.0] - Initial milestone
- Implemented keyword scanning (case-insensitive)
- Implemented basic IOC scanning (IPv4 + URL regex)
- Added CLI arguments (--input, --output, --matches)
- Added report generation + optional evidence file output
- Validated against real macOS log sources (not committed)

Planned next:
- Custom keyword lists via file input
- Context lines output (grep-like)
- Count exact number of IOCs (not just lines containing them)
- Refactor into modules for maintainability