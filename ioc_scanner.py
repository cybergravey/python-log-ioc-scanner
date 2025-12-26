import argparse
import re
from datetime import datetime

# Args
parser = argparse.ArgumentParser(description="Scan a log file for keywords and simple IOCs (IPs, URLs).")
parser.add_argument("--input", "-i", required=True, help="Path to the input log file.")
parser.add_argument("--output", "-o", default="ioc_report.txt", help="Path to the output report file.")
parser.add_argument("--matches", "-m", default="matched_lines.txt", help="File to write matched lines file")
parser.add_argument("--no-matches-file", action="store_true", help="Do not write matched lines file")
args = parser.parse_args()

log_file = args.input
report_file = args.output
matches_file = args.matches

# What to scan for
keywords = [
    "error", "failed", "failure", "denied", "unauthorized",
    "sudo", "authentication", "panic", "timeout", "disconnect"
]

# Simple regex patterns for IOCs
ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")
url_pattern = re.compile(r"\bhttps?://[^\s]*\b")

# Counters / storage
total_lines = 0
keyword_hits = {k: 0 for k in keywords}
ip_hits = 0
url_hits = 0
matched_lines = 0

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Scan
with open(log_file, "r") as f:
    for line in f:
        total_lines += 1
        raw = line.rstrip("\n")
        lower = raw.lower()

        line_matched = False

        # Keyword matches
        for k in keywords:
            if k in lower:
                keyword_hits[k] += 1
                line_matched = True

        # IOC matches (IPs / URLs)
        if ip_pattern.search(raw):
            ip_hits += 1
            line_matched = True

        # Save evidence
        if line_matched:
            matched_lines += 1
            if not args.no_matches_file:
                with open(matches_file, "a") as out:
                    out.write(raw + "\n")

# Build report
report_lines = []
report_lines.append("=== IOC / Keyword Scan Report ===")
report_lines.append(f"Generated: {timestamp}")
report_lines.append(f"Source file: {log_file}")
report_lines.append("")
report_lines.append("--- Summary ---")
report_lines.append(f"Total lines scanned: {total_lines}")
report_lines.append(f"Lines with any match: {matched_lines}")
report_lines.append(f"Lines with IPs: {ip_hits}")
report_lines.append(f"Lines with URLs: {url_hits}")
report_lines.append("")
report_lines.append("--- Keyword Hits (lines containing keywords) ---")

# Sort keywords by hit count (descending)
for k, count in sorted(keyword_hits.items(), key=lambda x: x[1], reverse=True):
    report_lines.append(f"{k}: {count}")

report = "\n".join(report_lines) + "\n"

print("\n" + report)

with open(report_file, "w") as f:
    f.write(report)

print(f"Saved report to: {report_file}")

if args.no_matches_file:
    print("Skipped matched lines file.")
else:
    print(f"Saved matched lines to: {matches_file}")