str1 = input("Enter the string: ")
ch = input("Enter the character: ")

if str1.startswith(ch) :
    print(f"{str1} starts with {ch}")
elif str1.endswith(ch) :
    print(f"{str1} ends with {ch}")