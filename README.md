# Server Resource Calculator

> A small Python script to collect and report CPU, RAM and disk usage in a human-readable terminal report. It is intended as an educational exercise or a simple local monitoring tool.

## Description

This repository contains an educational script named "Server Resource Calculator" (file: `1.2.py`) that uses the `psutil` library to gather system metrics and prints a formatted report to stdout, including a banner with a localized timestamp.

The script reports:
- Number of CPU cores (physical and logical)
- CPU usage (%)
- RAM usage (GB and %)
- Disk usage (TB and %)

The script prints warnings when any metric exceeds the default threshold of 80%.

## Requirements

- Python 3.9+ (recommended) — `zoneinfo` is available in the standard library from Python 3.9.
- `psutil` Python package.
- `os`, `zoneinfo` and `datetime` (standard library modules).

## Installation

1. (Optional but recommended) Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # for bash (Linux/macOS). In Windows PowerShell use: .\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install psutil
```

## Usage

Place the `1.2.py` file in the same directory as this README (or point to the correct path) and run:

```bash
python 1.2.py
```

The script requires no arguments; it collects current system metrics and prints a formatted report to stdout.

## Example output

Example of the script output (simplified):

```
+--------------------------------------------------------------+
|                                                              |
|            Server Resource Calculator                        |
|     Script to display CPU, RAM and Disk information          |
|           Initialization: 2025-11-14T10:32:05-03:00          |
|                                                              |
+--------------------------------------------------------------+

--- CPU usage ---
Physical CPU cores = 4
Logical CPU cores = 8
CPU usage (%) = 12.3%

--- RAM usage ---
RAM used = 5.123 GB
RAM total = 16.000 GB
RAM used (%) = 32.02%

--- Disk usage ---
Disk used = 0.45 TB
Disk total = 1.00 TB
Disk used (%) = 45.00%

```

When any metric exceeds 80%, the script prints a warning line (for example: "Warning: CPU usage above 80%").

## How it works (technical summary)

- Uses `psutil` to collect CPU, memory and disk metrics.
- Converts bytes to human-readable GB/TB and calculates percentages.
- Generates a localized timestamp using `zoneinfo.ZoneInfo("America/Sao_Paulo")` for the banner.

Contract (input/output):
- Input: none (reads local system information)
- Output: formatted text printed to stdout
- Errors: missing dependencies (e.g. `psutil`) will raise ImportError — install dependencies to fix

Known edge cases:
- Systems without timezone data available for `zoneinfo` (workaround: install `tzdata` or provide a timezone fallback)
- Restricted permission environments that block access to some statistics (rare for `psutil`)
- Running inside containers with limited visibility — reported values reflect the kernel/container view

## Testing and validation

This is a simple local script; there is no test suite included. Validate by running the script at different times and comparing results with OS-provided monitoring tools.

## Contributing

Small contributions are welcome (typo fixes, improving output, adding a CLI for configurable thresholds). Please open a Pull Request with a clear description of changes.

## License

MIT — feel free to reuse and adapt for educational purposes.
