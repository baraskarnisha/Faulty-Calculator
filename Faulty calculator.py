# faulty calculator 45*3 = 555
# 56+9 = 77
# 56/6 = 4

x = int(input("Enter a number: "))
y = int(input("Enter a second number: "))

z = input("what you want to do?" '+, -, *, /,')

if x == 45 and y == 3 and z == '*':
    print("555")
elif x == 56 and y == 56 and z == '+':
    print("77")
elif x == 56 and y == 6 and z == '/':
    print("4")
    # for Addition
elif z == '+':
    a = (x+y)
    print(a)
    # for Multiplication
elif z == '*':
    b = (x*y)
    print(b)
    # for Subtraction
elif z == '-':
    c = (x-y)
    print(c)
    # for Division 
elif z == '/':
    d = (x/y)
    print(d)
