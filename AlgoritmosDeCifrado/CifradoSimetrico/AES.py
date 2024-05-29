from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_aes(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt_aes(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return unpad(decrypted_message, AES.block_size).decode()

if __name__ == "__main__":
    message = "Este es un mensaje secreto"
    key = b'0123456789abcdef'  # Clave AES de 128 bits

    encrypted = encrypt_aes(message, key)
    decrypted = decrypt_aes(encrypted, key)

    print("Mensaje original:", message)
    print("Mensaje cifrado:", encrypted)
    print("Mensaje descifrado:", decrypted)
