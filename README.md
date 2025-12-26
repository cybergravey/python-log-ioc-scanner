# Python Log + IOC Scanner

A Python CLI tool that scans log files for:
- **keywords** (error, failed, denied, sudo, authentication, etc.)
- simple **IOCs** (IP addresses, URLs)
- outputs a **summary report** and an optional **matched lines** evidence file

Built as a fundamentals-first Python project focused on scripting, automation, and real-world log parsing.

## Features

- Streams large log files line-by-line (memory friendly)
- Keyword matching (case-insensitive)
- Basic IOC detection using regex (IPs, URLs)
- CLI interface using `argparse`
- Generates timestamped reports
- Optional evidence output file for matched lines

## Quick Start

### Run against a sample log
```bash

python3 ioc_scanner.py --input examples/sample.log --output examples/sample_report.txt --matches examples/sample_matches.txt 

```

### Run against a real macOS log (example)
```bash

python3 ioc_scanner.py --input /var/log/install.log --output install_ioc_report.txt --matches install_matches.txt

```

### CLI Help
```bash

python3 ioc_scanner.py --help

```

## Output

- *_report.txt: Summary counts and keywords hit totals
- *_matches.txt: Raw lines that matched any keyword/IOC (optional)

## Skills Demonstrated

- Python fundementals (variables, loops, conditionals, functions)
- File I/O (read/write)
- CLI tooling (argparse)
- Regular expression (re)
- Basic log parsing / security-minded pattern matching
- Report generation

## Roadmap

Enhancments will be documented in docs/CHANGELOG.md and Git tags/releases.

## Project History

This project was developed incrementally to reinforce Python fundamentals
and real-world scripting workflows. Earlier learning-stage scripts are
preserved in the `archive/` directory to demonstrate progression and
iterative development.