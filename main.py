class Faktorial:
    def __init__(self, son):
        self.son = son

    def faktorial_recursion(self):
        if self.son == 0 or self.son == 1:
            return 1
        else:
            return self.son * Faktorial(self.son - 1).faktorial_recursion()

    def faktorial_loop(self):
        faktorial = 1
        for i in range(1, self.son + 1):
            faktorial *= i
        return faktorial

def main():
    while True:
        print("1. Faktorialni recursion orqali hisoblash")
        print("2. Faktorialni loop orqali hisoblash")
        print("3. Chiqish")
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == "1":
            son = int(input("Sonni kiriting: "))
            faktorial = Faktorial(son)
            print(f"{son}! = {faktorial.faktorial_recursion()}")
        elif tanlov == "2":
            son = int(input("Sonni kiriting: "))
            faktorial = Faktorial(son)
            print(f"{son}! = {faktorial.faktorial_loop()}")
        elif tanlov == "3":
            break
        else:
            print("Noto'g'ri tanlov")

if __name__ == "__main__":
    main()