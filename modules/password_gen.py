import random
import string
import main

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def gen_password():
    try:
        length = int(input("Longueur du mot de passe ? [12]: ") or 12)
        if length < 4:
            print("4 characters minimum.")
        else:
            pwd = generate_password(length)
            print("Mot de passe généré :\n", pwd)
            input("Appuyez sur Entrée pour continuer...")  
            main.main()
    except ValueError:
        print("Entrée non valide.")
