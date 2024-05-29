import os
import gnupg

# Configurar una instancia de GnuPG
gpg = gnupg.GPG(gnupghome='/ruta/a/tu/carpeta/gnupg')

# Generar un par de claves
input_data = gpg.gen_key_input(key_type="RSA", key_length=2048)
key = gpg.gen_key(input_data)

# Mensaje a cifrar
message = "Este es un mensaje de ejemplo para cifrar con PGP"

# Cifrar el mensaje
encrypted_data = gpg.encrypt(message, key.fingerprint)

# Guardar el mensaje cifrado en un archivo
# with open("/ruta/a/tu/carpeta/mensaje_cifrado.asc", "w") as file:
#     file.write(str(encrypted_data))

# Descifrar el mensaje
decrypted_data = gpg.decrypt(str(encrypted_data), passphrase='tu_contraseña')

print('Mensaje descifrado:')
print(decrypted_data)
