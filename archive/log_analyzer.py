print("=== Log Analyzer ===")

log_file = "sample.log"

info_count = 0
error_count = 0
warning_count = 0
total_lines = 0
unknown_count = 0

with open(log_file, "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith("INFO"):
            info_count += 1
        elif line.startswith("ERROR"):
            error_count += 1
        elif line.startswith("WARNING"):
            warning_count += 1
        else:
            unknown_count += 1
        total_lines += 1

print("\n--- Log Summary ---")
print(f"INFO: {info_count / total_lines: .0%}")
print(f"ERROR: {error_count / total_lines: .0%}")
print(f"WARNING: {warning_count / total_lines: .0%}")
print(f"UNKNOWN: {unknown_count / total_lines: .0%}")
print(f"Total lines: {total_lines}")
        