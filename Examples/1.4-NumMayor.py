class MainClass:
    @staticmethod
    def main():
        num1 = int(input("Escribeme el primer numero: "))
        num2 = int(input("Escribeme el segundo numero: "))

        if num1 >= num2:
            print("El primer numero es mayor o igual que el segundo")
        else:
            print("El segundo numero es mayor que el primero")

if __name__ == "__main__":
    MainClass.main()
