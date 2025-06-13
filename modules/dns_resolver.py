import socket
import main

def dns_resolve_all(domain):
    try:
        infos = socket.getaddrinfo(domain, None)
        ips = sorted(set(item[4][0] for item in infos))
        print(f"{domain} =>")
        for ip in ips:
            print("  ", ip)
        return ips
    except Exception as e:
        print(f"Erreur pour {domain} : {e}")
        return []

def resolve_dns():
    domaine = input("Nom de domaine à résoudre: ").strip()
    dns_resolve_all(domaine)
    input("Appuyez sur Entrée pour continuer...")
    main.main()