from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_rsa(message, public_key):
    cipher = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_rsa(encrypted_message, private_key):
    cipher = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    message = "Este es un mensaje secreto"
    key = RSA.generate(2048)

    encrypted = encrypt_rsa(message, key.public_key())
    decrypted = decrypt_rsa(encrypted, key)

    print("Mensaje original:", message)
    print("Mensaje cifrado:", encrypted.hex())
    print("Mensaje descifrado:", decrypted)
