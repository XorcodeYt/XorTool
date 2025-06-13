import socket
from tqdm import tqdm
import main
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(ip, port, timeout=0.2):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return port
    except:
        pass
    return None

def scan_ports(ip, start_port=1, end_port=65535, max_workers=200):
    total_ports = end_port - start_port + 1
    print(f"Scan de {ip} - Ports {start_port} à {end_port} (threads={max_workers}) ...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(scan_port, ip, port) for port in range(start_port, end_port + 1)]
        for future in tqdm(as_completed(futures), total=total_ports, desc="Scanning ports"):
            port = future.result()
            if port:
                open_ports.append(port)
    print("Scan terminé.")
    if open_ports:
        print("Ports ouverts:", sorted(open_ports))
    else:
        print("Aucun port ouvert trouvé.")
    return open_ports

def start_scanner():
    ip = input("Entrez l'adresse IP à scanner: ").strip()
    try:
        start_port = int(input("Port de début [1]: ") or 1)
        end_port = int(input("Port de fin [65535]: ") or 65535)
    except ValueError:
        print("Entrée invalide pour les ports. Utilisation des valeurs par défaut (1 à 65535).")
        start_port, end_port = 1, 65535

    try:
        max_workers = int(input("Nombre de threads [200]: ") or 200)
    except ValueError:
        max_workers = 200

    scan_ports(ip, start_port, end_port, max_workers)
    input("Appuyez sur Entrée pour continuer...")
    main.main()