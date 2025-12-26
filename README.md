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
<img width="674" height="175" alt="Screenshot 2025-12-25 at 10 59 51 PM" src="https://github.com/user-attachments/assets/da59c2e4-f218-416b-aa1c-b05ff06cd103" />

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

<img width="440" height="483" alt="Screenshot 2025-12-25 at 10 56 24 PM" src="https://github.com/user-attachments/assets/e88b4adf-00cc-48d1-b500-a1c1acb445a2" />


- *_matches.txt: Raw lines that matched any keyword/IOC (optional)

<img width="675" height="164" alt="Screenshot 2025-12-25 at 10 56 05 PM" src="https://github.com/user-attachments/assets/01304cbd-6e40-4b4b-8b88-37493e5ffb26" />


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
