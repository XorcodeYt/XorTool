import subprocess
import re
import main

def list_windows_credentials():
    result = subprocess.run(['cmdkey', '/list'], capture_output=True, text=True)
    return result.stdout.splitlines()

def delete_xbox_and_xbltickets_credentials():
    lines = list_windows_credentials()
    # Keywords à chercher (insensible à la casse)
    keywords = ['xbox', 'xboxlive', 'xsts', 'live', 'xbltickets']
    targets_to_delete = []
    for line in lines:
        match = re.search(r'Target:\s*(.+)', line)
        if match:
            target = match.group(1)
            if any(kw.lower() in target.lower() for kw in keywords):
                targets_to_delete.append(target)
    if not targets_to_delete:
        print("Aucun credential Xbox/XblTickets trouvé.")
        return
    for target in targets_to_delete:
        print(f"Suppression de la credential : {target}")
        subprocess.run(['cmdkey', '/delete:' + target], capture_output=True, text=True)
    print("Suppression terminée.")

def clear_credentials():
    print("Attention cette fonctionalité n'a pas été testée et peut ne pas fonctionner correctement.")
    print("Aussi cette fonctionalité supprime les credentials Xbox/XblTickets de Windows.")
    input("Appuyez sur Entrée pour continuer pour annuler...")
    print("Suppression des credentials Xbox/XblTickets...")
    delete_xbox_and_xbltickets_credentials()
    print("Suppression terminée.")
    input("Appuyez sur Entrée pour continuer...")  
    main.main()