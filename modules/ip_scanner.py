import platform
import subprocess
import main
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_ip(ip):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout = "1"
    timeout_param = "-w" if platform.system().lower() == "windows" else "-W"
    command = ["ping", param, "1", timeout_param, timeout, ip]
    try:
        subprocess.check_output(command, stderr=subprocess.DEVNULL)
        return ip
    except subprocess.CalledProcessError:
        return None

def scan_ips(ip_input, max_workers=256):
    octets = ip_input.strip().split('.')
    active_ips = []

    if len(octets) == 2:
        ips = [f"{octets[0]}.{octets[1]}.{i}.{j}" for i in range(1, 255) for j in range(1, 255)]
        print(f"Scan de {ip_input}.1.1 à {ip_input}.254.254 ({len(ips)} IPs)")
    elif len(octets) == 3:
        ips = [f"{octets[0]}.{octets[1]}.{octets[2]}.{j}" for j in range(1, 255)]
        print(f"Scan de {ip_input}.1 à {ip_input}.254 ({len(ips)} IPs)")
    elif len(octets) == 4:
        ips = [ip_input]
        print(f"Scan de l'IP unique {ip_input}")
    else:
        print("Format d'IP non reconnu. Utilise 192.168 ou 192.168.1 ou 192.168.1.100")
        return []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(ping_ip, ip): ip for ip in ips}
        for future in tqdm(as_completed(futures), total=len(ips), desc="Scanning IPs", unit="ip"):
            result = future.result()
            if result:
                active_ips.append(result)

    print("\nScan terminé. IPs actives :")
    for ip in active_ips:
        print(ip)
    print(f"Total IPs actives trouvées: {len(active_ips)}")
    return active_ips

def start_scan():
    ip_input = input("Entrer une base d'IP à scanner: ").strip()
    scan_ips(ip_input)
    input("Appuyez sur Entrée pour continuer...")
    main.main()