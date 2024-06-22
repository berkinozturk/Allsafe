import os
import re

TARGET_FOLDER = r"C:\Users\safa1\OneDrive\Masaüstü\New folder (4)\Allsafe-main\Allsafe-main"


VIRUS_SIGNATURE_PATTERN = re.compile(r"s0fTw4R30pT1m1z4t10n\d*")

def scan_files():
    infected_files = []
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                if is_infected(file_path):
                    infected_files.append(file_path)
    return infected_files

def is_infected(file_path):
    with open(file_path, "r") as f:
        content = f.read()
    return bool(VIRUS_SIGNATURE_PATTERN.search(content))

def clean_files(infected_files):
    for file_path in infected_files:
        clean_file(file_path)

def clean_file(file_path):

    with open(file_path, "w") as f:
        f.write("")

def run_antivirus():
    print("Antivirus scanning started.")
    infected_files = scan_files()
    if infected_files:
        print(f"Found {len(infected_files)} infected files. Cleaning them now...")
        clean_files(infected_files)
        print("Cleaning completed.")
    else:
        print("No infected files found.")
    print("Antivirus scanning finished.")

if __name__ == "__main__":
    run_antivirus()