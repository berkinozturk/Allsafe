import os

# Virüs imzalarını saklayacağımız liste
VIRUS_SIGNATURES = ["s0fTw4R30pT1m1z4t10n"]

# Hedef dosya
TARGET_FILE = os.path.expanduser("~/Desktop/ornek.txt")

def detect_and_clean_file(file_path):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        infected = False
        for signature in VIRUS_SIGNATURES:
            if signature in content:
                infected = True
                break

        if infected:
            clean_file(file_path, content)
        else:
            print(f"Virüs tespit edilmedi: {file_path}")

    except Exception as e:
        print(f"Hata: {e}")

def clean_file(file_path, content):
    try:
        # Virüs imzasını ve "This file has been infected by a virus." metnini kaldırın
        clean_content = content.replace("This file has been infected by a virus.\n", "").strip()
        for signature in VIRUS_SIGNATURES:
            clean_content = clean_content.replace(signature, "").strip()
        
        with open(file_path, "w") as f:
            f.write(clean_content if clean_content else "Bu dosya temizlenmiştir.\n")
        print(f"Dosya temizlendi: {file_path}")
    except Exception as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    print("Antivirüs başlatılıyor...")
    detect_and_clean_file(TARGET_FILE)
    print("Tarama ve temizlik işlemi tamamlandı!")
