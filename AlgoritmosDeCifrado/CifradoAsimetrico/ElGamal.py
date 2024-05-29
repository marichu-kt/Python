from Crypto.PublicKey import ElGamal
from Crypto import Random
import random

def generate_key(p, g, x):
    y = pow(g, x, p)
    return (p, g, y), (p, g, x)

def encrypt_elgamal(message, public_key):
    p, g, y = public_key
    k = random.randint(1, p - 1)
    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p
    return c1, c2

def decrypt_elgamal(ciphertext, private_key):
    p, _, x = private_key
    c1, c2 = ciphertext
    s = pow(c1, p - 1 - x, p)
    return (c2 * s) % p

if __name__ == "__main__":
    # Parámetros de ejemplo
    p = 23
    g = 5
    x = 6  # Clave privada
    public_key, private_key = generate_key(p, g, x)

    # Mensaje a cifrar
    message = 19

    # Cifrado
    ciphertext = encrypt_elgamal(message, public_key)

    # Descifrado
    decrypted_message = decrypt_elgamal(ciphertext, private_key)

    print("Mensaje original:", message)
    print("Mensaje cifrado:", ciphertext)
    print("Mensaje descifrado:", decrypted_message)
