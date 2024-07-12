from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# FUNCION CIFRAR TEXTO
def encrypt_text(key, text):
    iv = get_random_bytes(AES.block_size)                                      # Genera un IV aleatorio del tamaño del bloque
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)      # Creamos objeto de cifrado AES
    encrypted_text = cipher.encrypt(pad(text.encode(), AES.block_size))        # Ciframos texto + añadimos relleno
    return base64.b64encode(iv + encrypted_text).decode('utf-8')               # Convertimos el objeto (bytes) en una cadena de texto (string)


# FUNCION DESCIFRAR TEXTO
def decrypt_text(key, encrypted_text):
    encrypted_data = base64.b64decode(encrypted_text)                           # Decodificamos el texto
    iv = encrypted_data[:AES.block_size]                                        # Extraemos el IV del tamaño del bloque
    encrypted_text = encrypted_data[AES.block_size:]                            # Extraemos el texto cifrado
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)       # Creamos objeto de descifrado AES
    decrypted_text = unpad(cipher.decrypt(encrypted_text), AES.block_size)      # Desciframos el texto + eliminamos relleno
    return decrypted_text.decode('utf-8')                                       # Convertimos el objeto (bytes) en una cadena de texto (string)

# INTERFAZ DE USUARIO
def main():
    while True:
        print("\n1. Cifrar texto")
        print("2. Descifrar texto")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            key = input("Introduce la clave de cifrado (16, 24 o 32 caracteres): ")
            text = input("Introduce el texto a cifrar: ")
            encrypted_text = encrypt_text(key, text)
            print(f"Texto cifrado: {encrypted_text}")

        elif choice == '2':
            key = input("Introduce la clave de cifrado (16, 24 o 32 caracteres): ")
            encrypted_text = input("Introduce el texto cifrado: ")
            try:
                decrypted_text = decrypt_text(key, encrypted_text)
                print(f"Texto descifrado: {decrypted_text}")
            except (ValueError, KeyError):
                print("Clave incorrecta o texto cifrado incorrecto.")

        elif choice == '3':
            break

        else:
            print("Opción no invalida")

if __name__ == "__main__":
    main()
