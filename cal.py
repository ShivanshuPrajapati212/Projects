print("Welcome To Calpy")

class Calculate:
    def __init__(self,num1,num2,operation):
         self.num1 = num1
         self.num2 = num2
         self.operation = operation
    
    def cal(self):
        if self.operation == '+':
            print(f"The sum of {self.num1} and {self.num2} is {self.num1+self.num2}")
        elif self.operation == '-':
            print(f"The sum of {self.num1} and {self.num2} is {self.num1-self.num2}")
        elif self.operation == '*':
            print(f"The sum of {self.num1} and {self.num2} is {self.num1*self.num2}")
        elif self.operation == '/':
            print(f"The sum of {self.num1} and {self.num2} is {self.num1/self.num2}")
        else:
            print("Try again...")



if __name__ == "__main__":
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))
    operator = input("Enter the operator : ")

    cal = Calculate(num1,num2,operator)

    print(cal.cal())