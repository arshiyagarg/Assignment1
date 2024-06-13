lst = []

while (True):
    str1 = input("Enter the string: ")
    if len(str1) ==  0:
        break
    lst.append(str1)

for i in lst:
    print(i)