# here i am going to build basic calculator
num1 = int(input("Enter the First Number : "))
num2 = int(input("Enter the Second Number : "))
print("OPERATIONS \n 1.add\n 2.sub\n 3.mul\n 4.div")
op = input("Enter the operations: ")


def add(num1,num2):
    resu = num1+num2
    print(f"Addition: {resu}")
def sub(num1,num2):
    resu = num1-num2
    return resu
def mul(num1,num2):
    resu = num1 * num2
    return resu
def div(num1,num2):
    resu = num1 / num2
    return resu

if op=='add':
    add(num1,num2)
elif op=='sub':
    result = sub(num1,num2)
    print(f"Subtraction : {result}")
elif op=='mul':
    result = mul(num1,num2)
    print(f"Multiplication : {result}")
elif op=='div':
    result = div(num1,num2)
    print(f"Division : {result}")
else:
    print("Requested op is not find")




