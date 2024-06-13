str1 = input("Enter the string: ")
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
temp = ""
for i in str1:
    if i in punctuation:
        continue
    else:
        temp += i

print(temp)
