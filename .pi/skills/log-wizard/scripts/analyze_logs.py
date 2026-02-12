import sys
import re

def analyze_log(file_path):
    patterns = [
        (re.compile(r'error', re.IGNORECASE), "ERROR"),
        (re.compile(r'fail', re.IGNORECASE), "FAILURE"),
        (re.compile(r'exception', re.IGNORECASE), "EXCEPTION"),
        (re.compile(r'stack trace', re.IGNORECASE), "STACK TRACE"),
        (re.compile(r'timeout', re.IGNORECASE), "TIMEOUT"),
    ]

    try:
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                for pattern, label in patterns:
                    if pattern.search(line):
                        print(f"[{label}] Line {line_num}: {line.strip()}")
                        break
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_logs.py <log_file>")
    else:
        analyze_log(sys.argv[1])
