n = int(input("Enter number of elements to be entered in list: "))
lst = []
for i in range(n):
    j = int(input("Enter: "))
    lst.append(j)

total = 0
for i in range(n):
    total += lst[i]

print(total)