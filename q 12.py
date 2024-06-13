num = int(input("Enter the number: "))
total = 0

while num != 0:
    total += num % 10
    num = int(num/10)

print(total)