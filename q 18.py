str1 = input("Enter the string: ")
str2 = input("Enter the string: ")
#
# str1.lower()
# str2.lower()

if sorted(str1.lower()) == sorted(str2.lower()):
    print("YES")
else:
    print("NO")