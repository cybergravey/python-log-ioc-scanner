import argparse
from datetime import datetime

# Argument parsing
parser = argparse.ArgumentParser(
    description="Analyze a log file and generate a summary report"
)

parser.add_argument(
    "--input",
    "-i",
    required=True,
    help="Path to the input log file",
)

parser.add_argument(
    "--output",
    "-o",
    default="log_report.txt",
    help="Path to the output report file (default: log_report.txt)"
)

args = parser.parse_args()

log_file = args.input
report_file = args.output

print("==== Log Analyzer ====")
print(f"Input file: {log_file}")
print(f"Output file: {report_file}")

# Counters
info_count = 0
error_count = 0
warning_count = 0
unknown_count = 0
total_lines = 0

# Read and analyze the log file
with open(log_file, "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        total_lines += 1

        if line.startswith("INFO"):
            info_count += 1
        elif line.startswith("ERROR"):
            error_count += 1
        elif line.startswith("WARNING"):
            warning_count += 1
        else:
            unknown_count += 1

# Helper function to calculate percentage
def pct(count:int, total: int) -> str:
    return f"{(count / total):.0%}" if total > 0 else "0%"

# Generate report
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

report = (
    "=== Log Report ===\n"
    f"Generated: {timestamp}\n"
    f"Source file: {log_file}\n\n"
    "--- Counts ---\n"
    f"INFO: {info_count}\n"
    f"ERROR: {error_count}\n"
    f"WARNING: {warning_count}\n"
    f"UNKNOWN: {unknown_count}\n"
    f"TOTAL LINES: {total_lines}\n\n"
    "--- Percentages ---\n"
    f"INFO: {pct(info_count, total_lines)}\n"
    f"ERROR: {pct(error_count, total_lines)}\n"
    f"WARNING: {pct(warning_count, total_lines)}\n"
    f"UNKNOWN: {pct(unknown_count, total_lines)}\n"
)

print("\n" + report)

# Write report to file
with open(report_file, "w") as out:
    out.write(report)

print(f"\nSaved report to {report_file}")