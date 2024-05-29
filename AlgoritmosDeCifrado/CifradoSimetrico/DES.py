from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_des(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_message = pad(message.encode(), DES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt_des(encrypted_message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return unpad(decrypted_message, DES.block_size).decode()

if __name__ == "__main__":
    message = "Este es un mensaje secreto"
    key = b'abcdefgh'  # Clave DES de 64 bits

    encrypted = encrypt_des(message, key)
    decrypted = decrypt_des(encrypted, key)

    print("Mensaje original:", message)
    print("Mensaje cifrado:", encrypted)
    print("Mensaje descifrado:", decrypted)
