n = int(input("Enter the range: "))
first = 0
second = 1

for i in range(2,n+2):
    print(first)
    temp = second
    second = first + temp
    first = temp

