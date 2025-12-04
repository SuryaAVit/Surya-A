class Calculator:
    def __init__(self,a,b,operate):
        self.a = a
        self.b = b
        self.operate = operate.lower()

    def Calculate(self):
        if self.operate == "add":
            return self.a + self.b
        elif self.operate == "subtract":
            return self.a - self.b
        elif self.operate == "multiply":
            return self.a * self.b
        elif self.operate == "divide":
            if self.b!=0:
                return self.a / self.b
            else:
                return "Division by zero!!Error!!"

a = float(input("Enter value a: "))
b = float(input("Enter value b: "))
operate = input("Enter operate(add, subtract, multiply, divide): ")

calcs = Calculator(a, b, operate)
print("Result: ",calcs.Calculate())
