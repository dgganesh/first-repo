fir=0
oper=""
sec=0


def add(num1,num2):
    return num1+num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def subtract(num1,num2):
    return num1-num2

func = {
    "=":add,
    "*":multiply,
    "/":divide,
    "-":subtract,
}


print("Type the first number")
fir=int(input())

print("Enter the operation either '+','-','/' or '*' ")
oper=input()

print("Enter the second number")
sec=int(input())

answer=func[oper](fir,sec)
print("Response is",answer)






