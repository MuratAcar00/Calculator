def calc(x,y,ops):
    if ops not in "+-*/":
        return "Only +,-,*,/"
    
    if ops == "+":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x+y))
    elif ops == "-":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x-y))
    elif ops == "*":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x*y))
    elif ops == "/":
        return(str(x) + " " + ops + " " + str(y) + " = " + str(x/y))
    
while True:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    ops = input("Chose between: +, -, *, /: ")

    print(calc(x,y,ops))