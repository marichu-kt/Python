import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Función para cifrar un archivo
def encrypt_file(key, input_file, output_file):
    # Generar un IV aleatorio
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)

    # Leer el contenido del archivo de entrada y cifrarlo
    with open(input_file, 'rb') as f:
        file_data = f.read()
    encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))

    # Guardar el IV y los datos cifrados en el archivo de salida
    with open(output_file, 'wb') as f:
        f.write(iv + encrypted_data)

# Función para descifrar un archivo
def decrypt_file(key, input_file, output_file):
    # Leer el IV y los datos cifrados del archivo de entrada
    with open(input_file, 'rb') as f:
        iv = f.read(AES.block_size)
        encrypted_data = f.read()

    # Crear el objeto de descifrado y descifrar los datos
    cipher = AES.new(pad(key.encode(), AES.block_size), AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

    # Guardar los datos descifrados en el archivo de salida
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Interfaz de usuario
def main():
    while True:
        print("\n1. Cifrar archivo")
        print("2. Descifrar archivo")
        print("3. Salir")
        choice = input("Selecciona una opción: ")

        if choice == '1':
            key = input("Introduce la clave de cifrado (16, 24 o 32 caracteres): ")
            input_file = input("Introduce la ruta del archivo a cifrar: ")
            output_file = input("Introduce la ruta del archivo cifrado de salida: ")
            encrypt_file(key, input_file, output_file)
            print(f"Archivo cifrado guardado en {output_file}")

        elif choice == '2':
            key = input("Introduce la clave de cifrado (16, 24 o 32 caracteres): ")
            input_file = input("Introduce la ruta del archivo cifrado: ")
            output_file = input("Introduce la ruta del archivo descifrado de salida: ")
            decrypt_file(key, input_file, output_file)
            print(f"Archivo descifrado guardado en {output_file}")

        elif choice == '3':
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
