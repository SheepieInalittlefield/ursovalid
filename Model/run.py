#!/usr/bin/env python3

import os
import subprocess
import sys

def main():
    """
    Script to run 'make req' for all Requirement property files.
    """

    properties_dir = "properties"

    # Ensure the properties directory exists
    if not os.path.isdir(properties_dir):
        print(f"Error: '{properties_dir}' directory not found!", file=sys.stderr)
        sys.exit(1)

    print(f"Searching for property files in '{properties_dir}/' starting with 'Requirement'...")
    print("------------------------------------------------------------------------")

    found_files = []
    try:
        # os.scandir is more efficient than os.listdir for checking file types
        with os.scandir(properties_dir) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.startswith("Requirement") and entry.name.endswith(".mcf"):
                    found_files.append(entry.path)
    except OSError as e:
        print(f"Error accessing directory '{properties_dir}': {e}", file=sys.stderr)
        sys.exit(1)

    if not found_files:
        print(f"No 'Requirement*.mcf' files found in '{properties_dir}/'.")
        print("Script finished.")
        return

    found_files.sort()  # Sort files for consistent processing order
    for prop_file in found_files:
        print(f"Processing property file: '{prop_file}'")

        try:
            # Run 'make req' with the property file
            # capture_output=True captures stdout and stderr
            # text=True decodes stdout/stderr as text
            # check=True will raise CalledProcessError if the command returns a non-zero exit code
            result = subprocess.run(
                ["make", "req", f"PROPERTY_FILE={prop_file}"],
                capture_output=True,
                text=True,
                check=True  # This makes it raise an exception on error
            )
            print(result.stdout.strip()) # Print make's stdout
            if result.stderr:
                print(result.stderr.strip(), file=sys.stderr) # Print make's stderr, if any

            print(f"Successfully processed '{prop_file}'.")

        except subprocess.CalledProcessError as e:
            print(f"Error: 'make req' failed for '{prop_file}'.", file=sys.stderr)
            print(f"Command: {e.cmd}", file=sys.stderr)
            if e.stdout:
                print(f"Stdout:\n{e.stdout.strip()}", file=sys.stderr)
            if e.stderr:
                print(f"Stderr:\n{e.stderr.strip()}", file=sys.stderr)
            # Decide whether to exit here or continue
            # For now, it continues like the shell script
            # sys.exit(1) # Uncomment to exit on first error
        except FileNotFoundError:
            print(f"Error: 'make' command not found. Please ensure 'make' is installed and in your PATH.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred while processing '{prop_file}': {e}", file=sys.stderr)
            # sys.exit(1) # Uncomment to exit on first error

        print("------------------------------------------------------------------------")

    print("Script finished.")

if __name__ == "__main__":
    main()