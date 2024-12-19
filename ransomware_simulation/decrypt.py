import os
from Crypto.Cipher import AES


def unpad(data):
    return data.rstrip(b' ')


def decrypt_file(file_path, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    decrypted_data = unpad(cipher.decrypt(encrypted_data))
    original_file_path = file_path[:-4]
    with open(original_file_path, 'wb') as f:
        f.write(decrypted_data)
    os.remove(file_path)


key = b'SixteenByteKey!l'

folder = 'dossier_confidentiel'

if os.path.exists(folder):
    print(f"Decrypting files in the folder : {folder}")
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path) and file_path.endswith('.enc'):
            decrypt_file(file_path, key)
            print(f"Decrypted file : {file_path[:-4]}")
    print("All files have been decrypted successfully.")
else:
    print(f"Error : The file '{folder}' is missing.")
