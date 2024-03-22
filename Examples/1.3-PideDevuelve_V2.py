class MainClass:
    @staticmethod
    def main():
        nombre = input("Escribe tu nombre: ")
        texto = input("Escribe tu edad: ")
        edad = int(texto)

        print("Te llamas", nombre, "y tienes", edad, "años")

if __name__ == "__main__":
    MainClass.main()
