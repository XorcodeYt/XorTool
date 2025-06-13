import os
import shutil
import re
from modules import ports_scanner, ip_scanner, dns_resolver, clear_credentials, password_gen, yt_dwn, zip_cracker

ANSI_ESCAPE = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')

def visible_len(text):
    return len(ANSI_ESCAPE.sub('', text))

def center_line(line: str) -> str:
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    padding = max((terminal_width - visible_len(line)) // 2, 0)
    return ' ' * padding + line

def rgb_gradient(start_rgb, end_rgb, steps):
    gradient = []
    for i in range(steps):
        ratio = i / max(steps - 1, 1)
        r = int(start_rgb[0] * (1 - ratio) + end_rgb[0] * ratio)
        g = int(start_rgb[1] * (1 - ratio) + end_rgb[1] * ratio)
        b = int(start_rgb[2] * (1 - ratio) + end_rgb[2] * ratio)
        gradient.append((r, g, b))
    return gradient

def print_ascii_art_with_gradient():
    art_lines = [
        "",
        "▒██   ██▒ ▒█████   ██▀███   ▄▄▄█████▓ ▒█████   ▒█████   ██▓    ",
        "▒▒▒█ █▒ ░▒██▒  ██▒▓██ ▒ ██▒▒▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    ",
        "░░▒▒█▒  ░▒██░  ██▒▓██ ░▄█▒▒▒▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    ",
        " ░▒█ █▒▒ ▒██   ██░▒██▀▀█▄▒  ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    ",
        "▒██▒ ▒██▒░ ████▓▒░░██▓ ▒██▒   ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒",
        "▒▒ ░ ░▓ ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░   ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░",
        "░░   ░▒ ░  ░ ▒ ▒░   ░▒ ░ ▒░     ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░",
        " ░    ░  ░ ░ ░ ▒    ░░   ░    ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   ",
        " ░    ░      ░ ░     ░                  ░ ░      ░ ░      ░  ░",
        ""
    ]

    light_violet = (230, 190, 255)
    dark_violet = (70, 0, 130)
    gradient_colors = rgb_gradient(light_violet, dark_violet, len(art_lines))

    for line, (r, g, b) in zip(art_lines, gradient_colors):
        colored = f"\033[38;2;{r};{g};{b}m{line}\033[0m"
        print(center_line(colored))

def real_length(s):
    ansi_escape = re.compile(r'\x1b\[.*?m')
    return len(ansi_escape.sub('', s))

def center_line(line):
    term_width = shutil.get_terminal_size().columns
    padding = max((term_width - real_length(line)) // 2, 0)
    return ' ' * padding + line

def display_fancy_menu(tools, title="|| MULTI  TOOL ||"):
    violet = "\033[38;2;200;100;255m"
    reset = "\033[0m"

    rows = [tools[i:i+3] for i in range(0, len(tools), 3)]
    col_widths = [0, 0, 0]
    for row in rows:
        for idx, tool in enumerate(row):
            col_widths[idx] = max(col_widths[idx], len(tool))
    menu_width = sum(col_widths) + 2 * 3 + 2
    menu_width = max(menu_width, len(title))
    border_top = "╔" + "═" * menu_width + "╗"
    border_mid = "╠" + "═" * menu_width + "╣"
    border_bottom = "╚" + "═" * menu_width + "╝"

    def format_row(row):
        line = "║"
        for i in range(3):
            if i < len(row):
                line += f" {row[i]:<{col_widths[i]}} "
            else:
                line += " " * (col_widths[i] + 2)
            if i < 2:
                line += "│"
        line += "║"
        return line

    print(center_line(f"{violet}{border_top}"))
    print(center_line(f"║{title:^{menu_width}}║"))
    print(center_line(border_mid))
    for row in rows:
        print(center_line(format_row(row)))
    print(center_line(f"{border_bottom}{reset}"))

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def launch_choise(selected_index):
    clear_terminal()
    if selected_index == 1:
        ports_scanner.start_scanner()
    elif selected_index == 2:
        ip_scanner.start_scan()
    elif selected_index == 3:
        dns_resolver.resolve_dns()
    elif selected_index == 4:
        clear_credentials.clear_credentials()
    elif selected_index == 5:
        password_gen.gen_password()
    elif selected_index == 6:
        yt_dwn.yt_dwn()
    elif selected_index == 7:
        zip_cracker.zip_cracker_launcher()
    elif selected_index == 8:
        print("XorTool - Multi Tool by Xorcode")
        print("Version 1.0 - 2025")
        print("=========================")
        print("ZIP Cracker uses the zip-cracker tool by Fresh Milkshake.")
        print("Repo: https://github.com/FreshMilkshake/zip-cracker")
        input("Appuyez sur Entrée pour continuer...") 
        main()
    elif selected_index == 9:
        print("Merci d'avoi utilisé XorTool !")
        input("Appuyez sur Entrée pour quitter...") 
        exit(0)
    else:
        print("Choix invalide. Veuillez sélectionner un outil valide.")
        input("Appuyez sur Entrée pour continuer...") 
        main()

def main():
    clear_terminal()
    print_ascii_art_with_gradient()
    tools = ["[1] TCP port Scanner", "[2] IP scanner", "[3] DNS Resolver",
             "[4] Clear credentials", "[5] Password Generator", "[6] YouTube Downloader",
             "[7] ZIP Cracker", "[8] Credits", "[9] Quitter"]
    display_fancy_menu(tools)
    try:
        choice = int(input(f"{"\033[38;2;250;150;255m"}=====> Select a tool [1-9]: "))
        if 1 <= choice <= 9:
            launch_choise(choice)
        else:
            print("Invalid choice. Enter a number from 1 to 9.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
