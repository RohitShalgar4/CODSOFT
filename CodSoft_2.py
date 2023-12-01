#let's start

def addtion(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return "Not able divide by zero"

def calculator():
    print("Calculator")
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))

    print("Choose Arithmetic opertion")
    print("1. Addition")
    print("2. Subtraction")
    print("3.Multiplication")
    print("4. Division")

    choice=input("Enter choice (1/2/3/4):")

    if choice in ['1','2','3','4']:
        if choice == '1':
            result=addtion(num1,num2)
        elif choice =='2':
            result=subtraction(num1,num2)
        elif choice =='3':
            result=multiplication(num1,num2)
        else:
            result= division(num1,num2)
        print("Result:",result)
    else:
        print("Error! Please enter valide choice")
if __name__=='__main__':
    calculator()
