#!/usr/bin/env python3
"""Remove duplicate/clear location entries from results.csv"""
import csv
import sys
from pathlib import Path

CSV_PATH = Path("/home/ali/clawd/seeker/db/results.csv")

def load_entries():
    if not CSV_PATH.exists():
        return []
    with open(CSV_PATH, 'r', newline='', encoding='utf-8') as f:
        return list(csv.reader(f))

def save_entries(rows):
    with open(CSV_PATH, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

def remove_by_index(indices):
    """Remove entries by 0-based index"""
    rows = load_entries()
    rows = [r for i, r in enumerate(rows) if i not in indices and r]  # keep non-empty
    save_entries(rows)
    print(f"Removed {len(indices)} entries. {len(rows)} remaining.")

def clear_all():
    """Clear all entries"""
    save_entries([])
    print("Cleared all entries.")

def list_entries():
    """List all entries with index"""
    rows = load_entries()
    if not rows:
        print("No entries.")
        return
    for i, r in enumerate(rows):
        if len(r) > 12:
            print(f"[{i}] {r[12]} {r[13]} ({r[0]})")
        else:
            print(f"[{i}] {r[0]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: cleanup.py <list|clear|remove N N N...>")
        sys.exit(1)
    
    cmd = sys.argv[1]
    if cmd == "list":
        list_entries()
    elif cmd == "clear":
        clear_all()
    elif cmd == "remove":
        indices = [int(x) for x in sys.argv[2:]]
        remove_by_index(indices)
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)
