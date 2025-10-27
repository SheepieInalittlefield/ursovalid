#!/usr/bin/env python3

import os
import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [-v] [pbes|graph] <req_num1> <req_num2> ...", file=sys.stderr)
        print("       -v: Enable verbose 'make' output (sets VERBOSE=1).", file=sys.stderr)
        print("       'pbes' is the default target if not specified.", file=sys.stderr)
        sys.exit(1)

    args = sys.argv[1:]

    # Check for the verbose flag and remove it from the list for further processing
    verbose_level = "0"
    if "-v" in args:
        verbose_level = "1"
        args.remove("-v")

    if not args:
        print("Error: No target or requirement numbers provided.", file=sys.stderr)
        sys.exit(1)

    # Determine make target and requirement numbers from the remaining arguments
    make_target = "pbes"  # Default target
    req_num_args = args
    if args[0] in ("pbes", "graph", "pbesnoce", "req"):
        make_target = args[0]
        req_num_args = args[1:]

    if not req_num_args:
        print("Error: No requirement numbers provided.", file=sys.stderr)
        sys.exit(1)

    try:
        req_numbers = {int(arg) for arg in req_num_args}
    except ValueError:
        print("Error: Requirement numbers must be integers.", file=sys.stderr)
        sys.exit(1)

    properties_dir = "properties"
    found_files = []
    missing_numbers = []

    for num in sorted(req_numbers):
        path = os.path.join(properties_dir, f"Requirement {num}.mcf")
        if os.path.isfile(path):
            found_files.append(path)
        else:
            missing_numbers.append(num)

    if missing_numbers:
        print(f"Warning: No property files found for requirement(s): {', '.join(map(str, missing_numbers))}", file=sys.stderr)

    if not found_files:
        print("No valid property files to process. Exiting.", file=sys.stderr)
        sys.exit(1)

    for prop_file in found_files:
        print(f"\n--- Running 'make {make_target}' for: {prop_file} ---")
        command = ["make", make_target, f"PROPERTY_FILE={prop_file}", f"VERBOSE={verbose_level}"]
        subprocess.run(command, check=True)

    print("\nScript finished.")

if __name__ == "__main__":
    main()