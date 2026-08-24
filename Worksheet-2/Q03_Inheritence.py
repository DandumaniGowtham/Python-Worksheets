class Numbers:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        print("Addition:", self.num1 + self.num2)

class Calculator(Numbers):
    def multiply(self):
        print("Multiplication:", self.num1 * self.num2)

calc = Calculator(10, 20)

calc.add()
calc.multiply()