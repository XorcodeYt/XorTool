import os
import subprocess
import main

INPUT_DIR = "zip-tool/input-zip"
OUTPUT_DIR = "zip-tool/output-zip"
DICT_DIR = "zip-tool/dictionarys"
ZIP_CRACKER_EXE = "modules/zip-cracker.exe"

def prepare_dirs():
    for d in [INPUT_DIR, OUTPUT_DIR, DICT_DIR]:
        if not os.path.exists(d):
            os.makedirs(d)
    if not os.listdir(INPUT_DIR):
        print(f"Place tes .zip dans '{INPUT_DIR}' puis relance.")
        main.main()
    return True

def list_zips():
    return [f for f in os.listdir(INPUT_DIR) if f.lower().endswith(".zip")]

def list_dicts():
    return [f for f in os.listdir(DICT_DIR) if os.path.isfile(os.path.join(DICT_DIR, f))]

def select_file(files, label="fichier"):
    if not files:
        print(f"Aucun {label} trouvé !")
        return None
    print(f"{label.capitalize()}s disponibles :")
    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")
    try:
        n = int(input(f"Numéro du {label} à utiliser ? "))
        assert 1 <= n <= len(files)
        return files[n-1]
    except:
        print("Choix invalide.")
        return None

def crack_zip_dict(zip_path, dict_path):
    command = [ZIP_CRACKER_EXE, zip_path, "--dict", dict_path, "--verbose"]
    print("\nLancement du cracker (dictionnaire)...\n")
    subprocess.run(command)
    print("\nCrack terminé.")

def crack_zip_bruteforce(zip_path):
    command = [ZIP_CRACKER_EXE, zip_path, "--generate", "--verbose"]
    print("\nLancement du cracker (bruteforce)...\n")
    subprocess.run(command)

def zip_cracker_launcher():
    if not prepare_dirs():
        input("Entrée pour continuer...")
        return
    zips = list_zips()
    zip_file = select_file(zips, "zip")
    if not zip_file:
        input("Entrée pour continuer...")
        return
    zip_path = os.path.join(INPUT_DIR, zip_file)
    print("\n[1] Crack par dictionnaire || [2] Crack par brute-force")
    choice = input("Ton choix [1/2] : ").strip()
    if choice == "1":
        dicts = list_dicts()
        dict_file = select_file(dicts, "dictionnaire")
        if not dict_file:
            input("Entrée pour continuer...")
            main.main()
        dict_path = os.path.join(DICT_DIR, dict_file)
        crack_zip_dict(zip_path, dict_path)
    elif choice == "2":
        crack_zip_bruteforce(zip_path)
    else:
        print("Entrez un choix valide")
        os.system("cls" if os.name == "nt" else "clear")
        zip_cracker_launcher()