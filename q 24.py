n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
op = input("Enter the operation (+,-,/,*) : ")

if op == '+':
    print(n1+n2)
elif op == '-':
    print(abs(n1-n2))
elif op == '*':
    print(n1*n2)
else:
    print(n1/n2)