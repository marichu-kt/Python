class MainClass:
    @staticmethod
    def Main(args):
        for i in range(1, 101):
            if i % 2 == 0 or i % 3 == 0:
                print(i)
        input()

if __name__ == "__main__":
    MainClass.Main(None)
