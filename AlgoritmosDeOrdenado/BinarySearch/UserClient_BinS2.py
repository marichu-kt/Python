import socket
import threading
import time

# Función para manejar la comunicación con un cliente específico
def manejar_cliente(cliente, direccion):
    print(f"Conexión establecida con {direccion}")

    while True:
        try:
            datos = cliente.recv(1024)
            if not datos:
                break
            mensaje = datos.decode()
            print(f"\nCliente {direccion}: {mensaje}")
            if mensaje.startswith("BSEARCH:"):
                numeros = [int(x) for x in mensaje.split(":")[1].split(",")]
                valor_a_buscar = int(mensaje.split(":")[2])
                indice = binary_search(numeros, valor_a_buscar)
                cliente.send(str(indice).encode())
        except ConnectionResetError:
            print(f"\nCliente {direccion} desconectado")
            break

    cliente.close()

# Función para enviar mensajes desde el servidor a un cliente específico
def enviar_mensaje(cliente):
    while True:
        try:
            mensaje = input("Servidor: ")
            cliente.send(mensaje.encode())
        except ConnectionResetError:
            print("Error de conexión. Intentando reconectar...")
            cliente.close()  # Cerrar el socket
            time.sleep(1)
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Volver a abrir el socket
            intentar_conectar(cliente)
            continue  # Continuar el bucle para volver a intentar enviar mensajes

# Función para intentar conectar el cliente al servidor
def intentar_conectar(cliente):
    while True:
        try:
            cliente.connect(('127.0.0.1', 8081))  # Puerto y IP del cliente
            break
        except ConnectionRefusedError:
            print("No se pudo establecer conexión. Reintentando ...")
            time.sleep(1)

# Función para buscar un elemento en una lista utilizando Búsqueda Binaria
def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Función principal del programa
def main():
    while True:
        try:
            servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            servidor.bind(('127.0.0.1', 8080))
            servidor.listen()    

            print("Esperando conexiones...")

            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            intentar_conectar(cliente)

            cliente_thread = threading.Thread(target=enviar_mensaje, args=(cliente,))
            cliente_thread.start()

            while True:
                cliente, direccion = servidor.accept()
                cliente_thread = threading.Thread(target=manejar_cliente, args=(cliente, direccion))
                cliente_thread.start()

        except Exception as e:
            print(f"Error: {e}")

        finally:
            servidor.close()
            cliente.close()

if __name__ == "__main__":
    main()
