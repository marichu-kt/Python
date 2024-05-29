from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_3des(message, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    padded_message = pad(message.encode(), DES3.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt_3des(encrypted_message, key):
    cipher = DES3.new(key, DES3.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return unpad(decrypted_message, DES3.block_size).decode()

if __name__ == "__main__":
    message = "Este es un mensaje secreto"
    
    # Generar una clave aleatoria de 24 bytes para Triple DES
    key = get_random_bytes(24)

    encrypted = encrypt_3des(message, key)
    decrypted = decrypt_3des(encrypted, key)

    print("Mensaje original:", message)
    print("Clave utilizada:", key.hex())
    print("Mensaje cifrado:", encrypted.hex())
    print("Mensaje descifrado:", decrypted)
