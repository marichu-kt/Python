# MODULOS NECESARIOS
import socket                                    # PARA LAS COMUNICACIONES EN RED
import threading                                 # PARA MANEJAR CONCURRENCIA
import base64                                    # PARA CODIFICACION/DECODIFICACION DE DATOS
from Crypto.PublicKey import RSA                 # PARA MANEJAR CLAVES RSA
from Crypto.Cipher import PKCS1_OAEP             # PARA EL CIFRADO/DECIFRADO RSA SEGURO

# CARGA LA CLAVE RSA PUBLICA
def cargar_clave_publica(archivo):
    with open(archivo, "rb") as f:               # ABRE EL ARCHIVO DE CLAVE PÚBLICA EN MODO LECTURA BINARIA
        clave = RSA.import_key(f.read())         # LEE E IMPORTA LA CLAVE PÚBLICA DEL ARCHIVO
    return PKCS1_OAEP.new(clave)                 # DEVUELVE EL OBJETO CIFRADO

# CARGA LA CLAVE RSA PRIVADA
def cargar_clave_privada(archivo):
    with open(archivo, "rb") as f:               # ABRE EL ARCHIVO DE CLAVE PRIVADA EN MODO LECTURA BINARIA
        clave = RSA.import_key(f.read())         # LEE E IMPORTA LA CLAVE PRIVADA DEL ARCHIVO
    return PKCS1_OAEP.new(clave)                 # DEVUELVE EL OBJETO CIFRADO

# FUNCIONES DE CIFRADO Y DESCIFRADO
def encrypt_text_rsa(cifra_publica, text):
    encrypted_text = cifra_publica.encrypt(text.encode())   # CIFRA EL TEXTO USANDO LA CLAVE PUBLICA Y LO CODIFICA
    return base64.b64encode(encrypted_text).decode('utf-8') # DEVUELVE EL TEXTO CODIFICADO

def decrypt_text_rsa(cifra_privada, encrypted_text):
    encrypted_data = base64.b64decode(encrypted_text)       # DECODIFICA EL TEXTO
    decrypted_text = cifra_privada.decrypt(encrypted_data)  # DESCIFRA EL TEXTO USANDO LA CLAVE PRIVADA
    return decrypted_text.decode('utf-8')                   # DEVUELVE EL TEXTO DECODIFICADO

# CARGA LAS CLAVES RSA
cifra_publica = cargar_clave_publica("clave_publica.pem")   # CARGA LA CLAVE PUBLICA D
cifra_privada = cargar_clave_privada("clave_privada.pem")   # CARGA LA CLAVE PRIVADA 

# FUNCIONES DE RED Y COMUNICACIÓN
def manejar_cliente(cliente, direccion):
    print(f"Conexión establecida con {direccion}")

    while True:
        try:
            datos = cliente.recv(1024)                      # RECIBE DATOS DEL CLIENTE (HASTA 1024 BYTES)
            if not datos:
                break
            mensaje = decrypt_text_rsa(cifra_privada, datos.decode()) # DESCIFRA EL MENSAJE USANDO LA CLAVE PRIVADA
            print(f"\nCliente {direccion}: {mensaje}")
        except (ConnectionResetError, ValueError, KeyError):
            print(f"\nCliente {direccion} desconectado o mensaje inválido")
            break

    cliente.close()                                         # CIERRA LA CONEXION 

def enviar_mensaje(cliente):
    while True:
        try:
            mensaje = input("Servidor: ")                   # SOLICITA AL USUARIO UN MENSAJE PARA ENVIAR AL CLIENTE
            mensaje_cifrado = encrypt_text_rsa(cifra_publica, mensaje) # CIFRA EL MENSAJE USANDO LA CLAVE PUBLICA
            cliente.send(mensaje_cifrado.encode())          # ENVÍA EL MENSAJE CIFRADO AL CLIENTE
        except ConnectionResetError:
            print("Error de conexión. Intentando reconectar...")
            cliente.close()                                 # CIERRA LA CONEXION
            time.sleep(1)
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # NUEVO SOCKET PARA EL CLIENTE
            intentar_conectar(cliente)                      # INTENTA RECONEXION CON EL CLIENTE
            continue

def intentar_conectar(cliente, ip, puerto):
    while True:
        try:
            cliente.connect((ip, puerto))                   # CONECTAR EL CLIENTE A LA IP Y PUERTO DEFINIDOS
            break
        except ConnectionRefusedError:
            print("No se pudo establecer conexión. Reintentando ...")
            time.sleep(1)

def main():
    ip_servidor = input("Introduce la IP del servidor UC2: ") # SOLICITA AL USUARIO LA IP DE UC2
    puerto_servidor = int(input("Introduce el puerto del servidor UC2: ")) # SOLICITA AL USUARIO EL PUERTO DE UC2
    
    ip_cliente = input("Introduce la IP del cliente UC1: ")  # SOLICITA AL USUARIO LA IP DE UC1
    puerto_cliente = int(input("Introduce el puerto del cliente UC1: ")) # SOLICITA AL USUARIO EL PUERTO DE UC1
    
    while True:
        try:
            servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # CREA UN SOCKET PARA EL SERVIDOR
            servidor.bind((ip_servidor, puerto_servidor)) # ASIGNA LA IP Y EL PUERTO AL SOCKET DEL SERVIDOR
            servidor.listen()                             # PONE EL SERVIDOR EN MODO ESCUCHA PARA ACEPTAR CONEXIONES ENTRANTES

            print("Esperando conexiones...")

            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # CREA UN SOCKET PARA EL CLIENTE
            intentar_conectar(cliente, ip_cliente, puerto_cliente) # LLAMA A LA FUNCION PARA INTENTAR CONECTAR AL CLIENTE

            cliente_thread = threading.Thread(target=enviar_mensaje, args=(cliente,)) # HILO PARA ENVIAR MENSAJES DESDE EL SERVIDOR AL CLIENTE
            cliente_thread.start()                          # HILO PARA ENVIAR MENSAJES

            while True:
                cliente_conectado, direccion = servidor.accept() # ACEPTA LA CONEXION
                cliente_thread = threading.Thread(target=manejar_cliente, args=(cliente_conectado, direccion)) # HILO PARA MANEJAR LA CONEXIÓN CON EL CLIENTE
                cliente_thread.start()                      # HILO PARA MANEJAR LA CONEXIÓN DEL CLIENTE

        except Exception as e:
            print(f"Error: {e}")

        finally:
            servidor.close()                                # CIERRA EL SOCKET DEL SERVIDOR
            cliente.close()                                 # CIERRA EL SOCKET DEL CLIENTE

if __name__ == "__main__":
    main()
