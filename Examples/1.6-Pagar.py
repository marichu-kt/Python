class MainClass:
    @staticmethod
    def main():
        precio = float(input("Escribe el precio del producto: "))
        forma = input("Escribe la forma de pago: tarjeta o efectivo: ").lower()

        if forma == "tarjeta":
            numero_cuenta = input("Introduce el número de tarjeta: ")
            print(f"El producto con precio {precio} se ha pagado con el número de cuenta {numero_cuenta}")
        elif forma == "efectivo":
            print(f"El producto con precio {precio} se ha pagado")
        else:
            print("La forma de pago no es correcta")

if __name__ == "__main__":
    MainClass.main()
