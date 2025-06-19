print("welcome to simple calculator")

num1=float(input("enter number 1"))
op=input('enter operator(+,-,*,\):')
num2=float(input("enter number 2:"))

if op=="+":
    print("result is ", num1+num2)
elif op == "-":
    print("result is ",num1-num2)
elif op == '*':
    print("result is ",num1*num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")
