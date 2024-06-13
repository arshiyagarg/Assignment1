inpType = input("Enter for c celsius convension and f farhenite: ")

if inpType=="c" :
    inp = float(input("Enter temperature in celsius: "))
    ans = (inp * 9 / 5) + 32
    print("The temprature in farhenite is : ",ans)
else:
    inp = float(input("Enter temperature in farhenite: "))
    ans = (5*(inp-32))/9
    print("The temprature in farhenite is : ", ans)
