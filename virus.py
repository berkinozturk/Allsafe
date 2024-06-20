import os

VIRUS_SIGNATURE = "softwareOptimization"

TARGET_FOLDER = os.path.expanduser("~/Desktop/virus")


def infect_files():
    for root, dirs, files in os.walk(TARGET_FOLDER):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                infect(file_path)


def infect(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    # check if it is already infected
    if VIRUS_SIGNATURE not in content:
        with open(file_path, "w") as f:
            f.write(content + "\n" + VIRUS_SIGNATURE)


def trigger_virus():
    print("Virüs aktif!")


if __name__ == "__main__":
    infect_files()
    trigger_virus()
