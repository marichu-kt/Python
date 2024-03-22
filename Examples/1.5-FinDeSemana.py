class MainClass:
    @staticmethod
    def main():
        dia = input("Escribe un día de la semana: ")

        if dia.lower() in ["lunes", "martes", "miércoles", "jueves", "viernes"]:
            print("No es fin de semana")
        elif dia.lower() in ["sábado", "domingo"]:
            print("Es fin de semana")
        else:
            print("Ese día no es correcto")

if __name__ == "__main__":
    MainClass.main()
